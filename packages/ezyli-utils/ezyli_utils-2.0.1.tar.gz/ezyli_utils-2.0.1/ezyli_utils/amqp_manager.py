import pika
import logging
import threading
import time
import json
from pika.exchange_type import ExchangeType
from pika.exceptions import ChannelClosed, AMQPConnectionError
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from .validator import validate_data
from .schemas import COMMON_SCHEMA

logger = logging.getLogger(__name__)


def construct_url(
    url,
    heartbeat=None,
    connection_attempts=None,
    retry_delay=None,
):
    """
    Heartbeats: RabbitMQ uses a heartbeat mechanism to detect if a client is still alive.
    If the client doesn't send any data for a certain period of time (the heartbeat interval),
    RabbitMQ will close the connection. You should ensure that your client sends data
    frequently enough to keep the connection alive.

    > The url_parts[4] refers to the query component of the URL.
    When you parse a URL using urlparse, it returns a 6-tuple
    containing the following components: scheme, netloc, path, params, query, and fragment.
    The query component is at index 4.
    """
    url_parts = list(urlparse(url))
    query = dict(parse_qs(url_parts[4]))
    if heartbeat is not None:
        query.update({"heartbeat": heartbeat})
    if connection_attempts is not None:
        query.update({"connection_attempts": connection_attempts})
    if retry_delay is not None:
        query.update({"retry_delay": retry_delay})

    url_parts[4] = urlencode(query)

    return urlunparse(url_parts)


class AMQPManager:
    """
    >> The lock is used to ensure thread safety. In multi-threaded environments,
     it's possible for multiple threads to access and modify shared data simultaneously.
     This can lead to inconsistent state and hard-to-debug issues.
     The lock object is a synchronization primitive that can be used to ensure that
     only one thread can enter a particular section of code at a time. In the context
     of the `AMQPHandler` class, the lock is used to ensure that only one thread
     can use the `channel` object at a time, preventing potential race conditions.
    """

    def __init__(
        self,
        url,
        heartbeat=None,
        connection_attempts=None,
        retry_delay=None,
        use_singleton=True,
    ):  
        print("AMQPManager :: __init__")
        # url = construct_url(
        #     url=url,
        #     heartbeat=heartbeat,
        #     connection_attempts=connection_attempts,
        #     retry_delay=retry_delay,
        # )
        url = url
        print(f"AMQP URL: {url}")
        self.params = pika.URLParameters(url)
        self.connection = None
        self.channel = None
        self.connect_counter = 0
        # add a lock for thread safety
        self.lock = threading.Lock()

    def connect(self, retry=True):
        with self.lock:
            self._connect(retry=retry)

    def publish(
        self,
        routing_key,
        message,
        exchange_name="",  # Default exchange
        content_type=None,
        max_retries=5,
        delivery_mode=2,
    ):
        with self.lock:
            self._publish(
                routing_key=routing_key,
                message=message,
                exchange_name=exchange_name,
                content_type=content_type,
                max_retries=max_retries,
                delivery_mode=delivery_mode,
            )

    def consume(
        self,
        queue,
        callback,
        validate_common_schema=False,
    ):
        with self.lock:
            self._consume(
                queue=queue,
                callback=callback,
                validate_common_schema=validate_common_schema,
            )

    def exchange_declare(
        self,
        exchange_name,
        exchange_type: ExchangeType,
        durable=False,
        retry_conn=False,
    ):
        with self.lock:  # use the lock
            try:
                if self.channel is None:
                    self.connect(retry=retry_conn)
                self.channel.exchange_declare(
                    exchange=exchange_name,
                    exchange_type=exchange_type,
                    durable=durable,
                )
                logger.info(f"Exchange {exchange_name} declared")
            except pika.exceptions.ChannelClosedByBroker as e:
                if "PRECONDITION_FAILED" in str(e):
                    logger.warning(
                        f"Exchange {exchange_name} already exists with different properties. Using the existing exchange."
                    )
                    # Reconnect to get a new channel after the exception
                    self.connect(retry=retry_conn)
                else:
                    logger.error(
                        f"An error occurred when trying to declare exchange: {e}"
                    )
            except Exception as e:
                logger.error(f"An error occurred when trying to declare exchange: {e}")

    def queue_declare(
        self,
        queue_name,
        durable=False,
        retry_conn=False,
    ):
        with self.lock:  # use the lock
            try:
                if self.channel is None:
                    self.connect(retry=retry_conn)
                self.channel.queue_declare(queue=queue_name, durable=durable)
                logger.info(f"Queue {queue_name} declared")
            except pika.exceptions.ChannelClosedByBroker as e:
                if "PRECONDITION_FAILED" in str(e):
                    logger.warning(
                        f"Queue {queue_name} already exists with different properties. Using the existing queue."
                    )
                    # Reconnect to get a new channel after the exception
                    self.connect(retry=retry_conn)
                else:
                    logger.error(f"An error occurred when trying to declare queue: {e}")
            except Exception as e:
                logger.error(f"An error occurred when trying to declare queue: {e}")

    def queue_bind(
        self,
        queue_name,
        exchange_name,
        routing_key,
        retry_conn=False,
    ):
        with self.lock:  # use the lock
            try:
                if self.channel is None:
                    self.connect(retry=retry_conn)
                self.channel.queue_declare(queue=queue_name)
                self.channel.queue_bind(
                    exchange=exchange_name,
                    queue=queue_name,
                    routing_key=routing_key,
                )
                logger.info(f"Queue {queue_name} bound to exchange {exchange_name}")
            except Exception as e:
                logger.error(f"An error occurred when trying to bind queue: {e}")

    def queue_unbind(
        self,
        queue_name,
        exchange_name,
        routing_key,
        retry_conn=False,
    ):
        with self.lock:  # use the lock
            try:
                if self.channel is None:
                    self.connect(retry=retry_conn)
                self.channel.queue_unbind(
                    exchange=exchange_name,
                    queue=queue_name,
                    routing_key=routing_key,
                )
                logger.info(f"Queue {queue_name} unbound from exchange {exchange_name}")
            except Exception as e:
                logger.error(f"An error occurred when trying to unbind queue: {e}")
    

    def _connect(self, retry=True):
        while True:
            self.connect_counter += 1
            try:
                if self.connection and self.connection.is_open:
                    # This is to avoid creating a new connection if the current one is still open
                    # Given that we are now using lock(), it is possible that the first thread
                    # that calls this method will create a new connection, and the second thread
                    # does not need to create a new connection if the first thread had established it
                    break
                self.close()
                self.connection = pika.BlockingConnection(self.params)
                self.channel = self.connection.channel()
                # Reset the counter if the connection is successful
                self.connect_counter = 0
                break  # If the connection is successful, break the loop
            except pika.exceptions.AMQPConnectionError as e:
                if not retry:
                    raise
                logger.error(f"An error occurred when trying to connect: {e}")
                time.sleep(5) if self.connect_counter > 1 else time.sleep(0)
            except Exception as e:
                logger.error(f"An unexpected error occurred: {e}")
                break

    def _publish(
        self,
        routing_key,
        message,
        exchange_name="",  # Default exchange
        content_type=None,
        max_retries=5,
        delivery_mode=2,
    ):
        """
        # delivery_mode=2 make message persistent
        """
        retries = 0
        while retries <= max_retries:
            try:
                if self.channel is None:
                    self.connect(retry=False)
                    if self.channel is None:
                        raise Exception("Failed to establish connection")
                self.channel.basic_publish(
                    exchange=exchange_name,
                    routing_key=routing_key,
                    body=message,
                    properties=pika.BasicProperties(
                        delivery_mode=delivery_mode,
                        content_type=content_type,
                    ),
                )
                logger.info(
                    f"Published message to {exchange_name} with routing key {routing_key}"
                )
                break  # If the operation is successful, break the loop
            except Exception as e:
                logger.info("Connection was closed, retrying...")
                retries += 1
                if retries > max_retries:
                    raise  # If max retries reached, re-raise the last exception
                try:
                    # Wait before retrying
                    time.sleep(5)
                    self.connect(retry=False)
                except Exception as e:
                    logger.error(f"An error occurred when trying to reconnect: {e}")

    def _consume(
        self,
        queue,
        callback,
        validate_common_schema=False,
    ):
        def internal_callback(ch, method, properties, body):
            if not validate_common_schema or self._is_valid_body(body):
                callback(ch, method, properties, body)

        while True:
            logger.info("Setting up consumer :- ...")
            if self.channel is None:
                self.connect()
            try:
                self.channel.basic_consume(
                    queue=queue,
                    on_message_callback=internal_callback,
                    auto_ack=True,
                )

                logger.info("Started Consuming...")

                self.channel.start_consuming()
            except (
                pika.exceptions.ChannelClosed,
                pika.exceptions.AMQPConnectionError,
            ) as e:
                logger.info("Reconnecting ...")
                self.reconnect()
            except Exception as e:
                logger.info("Reconnecting ...")
                logger.error(e)
                self.reconnect()

    def close(self):
        with self.lock:  # use the lock
            try:
                if self.channel is not None:
                    self.channel.close()
                if self.connection is not None:
                    self.connection.close()
            except Exception as e:
                logger.error(
                    f"An error occurred when trying to close the connection: {e}"
                )

    def reconnect(self):
        self.connect()

    def validate_data(self, data, schema):
        return validate_data(data, schema)

    def _is_valid_body(self, body):
        # Convert body from bytes to string and then to a dictionary
        try:
            content = json.loads(body.decode())
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON received :: {body.decode()}")
            return False
        schema = COMMON_SCHEMA
        return self.validate_data(content, schema)
