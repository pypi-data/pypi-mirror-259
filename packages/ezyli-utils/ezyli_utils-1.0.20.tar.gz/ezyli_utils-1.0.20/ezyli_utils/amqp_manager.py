import pika
import time
from .validator import validate_data
from .schemas import COMMON_SCHEMA
from pika.exceptions import ChannelClosed, AMQPConnectionError
import json


class AMQPManager:
    def __init__(self, amqp_url):
        self.params = pika.URLParameters(amqp_url)
        self.connection = None
        self.channel = None
        self.connect_counter = 0

    def connect(self, retry=True):
        while True:
            self.connect_counter += 1
            try:
                self.close_connection()
                self.connection = pika.BlockingConnection(self.params)
                self.channel = self.connection.channel()
                # Reset the counter if the connection is successful
                self.connect_counter = 0
                break  # If the connection is successful, break the loop
            except pika.exceptions.AMQPConnectionError:
                if not retry:
                    raise
                print("Failed to connect, retrying...")
                time.sleep(5) if self.connect_counter > 1 else time.sleep(0)
            except Exception as e:
                if not retry:
                    raise
                print(f"An error occurred when trying to connect: {e}")
                time.sleep(5) if self.connect_counter > 1 else time.sleep(0)

    def close_connection(self):
        try:
            if self.connection:
                self.connection.close()
        except Exception as e:
            print(f"An error occurred when trying to close the connection: {e}")

    def reconnect(self):
        self.connect()

    def publish(
        self,
        queue,
        message,
        durability,
        content_type=None,
        max_retries=5,
    ):
        retries = 0
        while retries <= max_retries:
            try:   
                if self.channel is None:
                    self.connect(retry=False)
                    if self.channel is None:
                        raise Exception("Failed to establish connection")
                self.channel.queue_declare(queue=queue, durable=durability)
                self.channel.basic_publish(
                    exchange="",
                    routing_key=queue,
                    body=message,
                    properties=pika.BasicProperties(
                        delivery_mode=2,
                        content_type=content_type,
                    ),  # delivery_mode=2 make message persistent
                )
                break  # If the operation is successful, break the loop
            except Exception as e:
                print("Connection was closed, retrying...")
                retries += 1
                if retries > max_retries:
                    raise  # If max retries reached, re-raise the last exception
                try:
                    # Wait before retrying
                    time.sleep(5)
                    self.connect(retry=False)  
                except Exception as e:
                    print(f"An error occurred when trying to reconnect: {e}")
    def validate_data(self, data, schema):
        return validate_data(data, schema)

    def _is_valid_body(self, body):
        # Convert body from bytes to string and then to a dictionary
        try:
            content = json.loads(body.decode())
        except json.JSONDecodeError:
            print(f"Invalid JSON received :: {body.decode()}")
            return False
        schema = COMMON_SCHEMA
        return self.validate_data(content, schema)

    def consume(
        self,
        queue,
        durability,
        callback,
        validate_common_schema=False,
    ):
        def internal_callback(ch, method, properties, body):
            if not validate_common_schema or self._is_valid_body(body):
                callback(ch, method, properties, body)

        while True:
            print("Setting up consumer 2:- ...")
            if self.channel is None:
                self.connect()
            try:
                self.channel.queue_declare(queue=queue, durable=durability)
                self.channel.basic_consume(
                    queue=queue,
                    on_message_callback=internal_callback,
                    auto_ack=True,
                )

                print("Started Consuming")

                self.channel.start_consuming()
            except (
                pika.exceptions.ChannelClosed,
                pika.exceptions.AMQPConnectionError,
            ) as e:
                print("Reconnecting ...")
                self.reconnect()
            except Exception as e:
                print("Reconnecting ...")
                print(e)
                self.reconnect()
