# Importing modules #
import os
import time
import threading
import kafka_sender
import data_generator
from logger import log

# Environment variables #
bid_size = int(os.environ.get('BID_SIZE', 50))
ask_size = int(os.environ.get('ASK_SIZE', 50))
random_start = int(os.environ.get('RANDOM_START', 1))
random_decimal = int(os.environ.get('RANDOM_DECIMAL', 1))
create_report_inteval = float(os.environ.get('CREATE_REPORT_INTERVAL', 0.1))
kafka_bootstrap_servers = os.environ.get(
                                        'KAFKA_BOOTSTRAP_SERVERS',
                                        'kafka:9092'
                                    )
kafka_topic = os.environ.get('KAFKA_TOPIC', 'metrics_raw')

KAFKA = kafka_sender.Kafka(kafka_bootstrap_servers)
GENERATOR = data_generator.Generator(
                                random_start,
                                random_decimal,
                                bid_size,
                                ask_size
                            )


# Function for multithreading #
def create_transfer():
    report = GENERATOR.generate_report()
    KAFKA.send_message(report, kafka_topic)


# Main function #
def main():
    log.info("main(): >>> Starting tool")
    while True:
        thread_job = threading.Thread(target=create_transfer, args=())
        thread_job.start()
        time.sleep(create_report_inteval)


if __name__ == "__main__":
    main()
