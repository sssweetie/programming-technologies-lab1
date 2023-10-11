# -*- coding: utf-8 -*-
from Types import DataType
from abc import ABC, abstractmethod


class DataReader(ABC):
    @abstractmethod
    def read(self, path: str) -> DataType:
        pass

class NewDataReader(DataReader):
    def read(self, path: str) -> DataType:
        with open(path, 'r') as file:
            data = json.load(file)
            return data  