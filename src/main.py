# -*- coding: utf-8 -*-
import argparse
import sys
import os
import pytest
import json
from Types import DataType
from StudentManager import StudentManager
from DataReader import DataReader
from JsonDataReader import JsonDataReader
from TextDataReader import TextDataReader
from CalcRating import CalcRating

def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path

def get_current_reader(path: str) -> DataReader:
    root, file_extension = os.path.splitext(path)  
    match file_extension:
        case ".txt":
            return TextDataReader()
        case ".json":
            return JsonDataReader()
        case _:
            raise ValueError("Неподдерживаемый формат")

def main():
    print(sys.argv[1:])

    path = get_path_from_arguments(sys.argv[1:])
    reader = get_current_reader(path)
    students = reader.read(path)
    rating = CalcRating(students).calc()
    min_score = 90
    min_subjects = 2
    student_manager = StudentManager(students)
    student_manager.find_and_print_qualified_student(min_score, min_subjects)
    print("Rating: ", rating)


if __name__ == "__main__":
    main()


class TestJsonDataReader:
    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = '''
        {
            "Иванов Иван Иванович": {
                "математика": 67,
                "литература": 100,
                "программирование": 91
            },
            "Петров Петр Петрович": {
                "математика": 78,
                "химия": 87,
                "социология": 61
            }
        }
        '''
        data = {
            "Иванов Иван Иванович": [
                ("математика", 67),
                ("литература", 100),
                ("программирование", 91)
            ],
            "Петров Петр Петрович": [
                ("математика", 78),
                ("химия", 87),
                ("социология", 61)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.json")
        p.write_text(json.dumps(file_and_data_content,
                     ensure_ascii=False),
                     encoding='utf-8')
        return str(p), file_and_data_content

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = JsonDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
