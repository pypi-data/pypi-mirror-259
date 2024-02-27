import logging
from typing import Union

import pymongo

from komoutils.core import KomoBase


class MongoDBReaderWriter(KomoBase):

    def __init__(self, uri: str, db_name: str, collection: str):
        self.client: pymongo.MongoClient = pymongo.MongoClient(uri)
        self.db = self.client[db_name]
        self.collection: str = collection

    @property
    def name(self):
        return "mongodb_reader_writer"

    def start(self):
        pass

    def read(self, filters: dict, omit: dict, limit: int = 1000000):
        records: list = list(self.db[self.collection].find(filters, omit).sort('_id', -1).limit(limit=limit))
        return records

    def write(self, data: Union[list, dict]):
        if len(data) == 0:
            self.log_with_clock(log_level=logging.INFO,
                                msg=f"0 records to send for collection {self.collection}. ")
            return
        # print(f"++++++++++++++++++++++++++++++++++++++++++++++++")
        try:
            if isinstance(data, dict):
                self.db[self.collection].insert_one(data)
            elif isinstance(data, list):
                self.db[self.collection].insert_many(data)

            self.log_with_clock(log_level=logging.DEBUG, msg=f"Successfully sent {self.collection} with size "
                                                             f"{len(data)} data to database. ")
            return 'success'
        except Exception as e:
            self.log_with_clock(log_level=logging.ERROR, msg=f"Unspecified error occurred. {e}")

    def updater(self, filters: dict, updater: dict):
        if len(updater) == 0:
            self.log_with_clock(log_level=logging.INFO,
                                msg=f"0 records to send for {self.db.upper()} for collection {self.collection}. ")
            return

        result = self.db[self.collection].update_one(filter=filters, update=updater, upsert=True)
        return result
