# Importing modules #
from logger import log
import kafka


class Kafka:

    def __init__(self, kafka_servers: str) -> None:
        log.info("Kafka.__init__: initing kafka sender")
        self.kafka_servers = kafka_servers
        self.kafka_producer = kafka.KafkaProducer(
                                        bootstrap_servers=self.kafka_servers
                                    )

    # Sending messages to kafka topic #
    def send_message(self, message: str, topic_name: str):
        log.info("Kafka.send_message: sending message in kafka...")
        try:
            key = bytes("message", encoding='utf-8')
            value = bytes(str(message), encoding='utf-8')
            response = self.kafka_producer.send(
                                                topic_name,
                                                key=key,
                                                value=value
                                           )
            response = response.get(
                                    timeout=60
                                )
            self.kafka_producer.flush()
            log.info(
                    f"Kafka.send_message: sending message in kafka: "
                    f"{response}"
                )
        
        except Exception as ex:
            log.error(
                    f"Kafka.send_message: exception send message in kafka: "
                    f"{ex}"
                )
