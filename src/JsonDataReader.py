# -*- coding: utf-8 -*-
import json
from Types import DataType
from DataReader import DataReader


class JsonDataReader(DataReader):
    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            data = json.load(file)

        students: DataType = {}
        for name, subjects in data.items():
            student_scores = []
            for subject, score in subjects.items():
                student_scores.append((subject, score))
            students[name] = student_scores

        return students
