from base.log import log
from base.interface import StorerInterface


class Console(StorerInterface):

    def store(self, data_list):
        for item in data_list:
            log.info(f"item info: {item}")

