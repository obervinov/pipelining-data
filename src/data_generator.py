# Importing modules #
import json
import statistics
import time
import random
from logger import log


class Generator:

    def __init__(
            self,
            random_start: int,
            random_decimal: int,
            bid_size: int,
            ask_size: int
    ) -> None:
        self.random_start = random_start
        self.random_decimal = random_decimal
        self.bid_size = bid_size
        self.ask_size = ask_size
        log.info("Generator.__init__: initing generator")

    # Generating a random float value with the specified range #
    def random_float_value(self, random_stop: int):
        return round(
                    random.uniform(
                        self.random_start, random_stop
                    ),
                    self.random_decimal
                )

    # Generating a dictionary with a report for further sending #
    def generate_report(self):
        report = dict()
        bid_list = list()
        ask_list = list()

        # Creating a timestamp in Unix format
        report = {'timestamp': time.time()}

        log.info(f"Generator.generate_report: creating report {report}")

        # Generate an array of BID and their values
        # and add them to the dictionary
        for bid_i in range(1, self.bid_size + 1):
            bid_value = self.random_float_value(bid_i * 10)
            bid_list.append(bid_value)

            report.update({f'bid_{bid_i}': bid_value})

        # Generate an array of ASK and their values
        # and add them to the dictionary
        for ask_i in range(1, self.ask_size + 1):
            ask_value = self.random_float_value(ask_i * 10)
            ask_list.append(ask_value)

            report.update({f'ask_{ask_i}': ask_value})

        # Calculate the average value for ASK and BID and adding objects to JSON
        bid_avg = round(statistics.fmean(bid_list), self.random_decimal)
        ask_avg = round(statistics.fmean(ask_list), self.random_decimal)
        # Adding json to the report dictionary

        # report.update({"stats": {"bid_avg": [bid_avg], "ask_avg": [ask_avg]}})
        report.update({"stats": [bid_avg, ask_avg]})

        return json.dumps(report)
