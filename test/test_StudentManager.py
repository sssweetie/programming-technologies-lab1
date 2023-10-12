import pytest
from StudentManager import StudentManager
from Types import DataType


class TestStudentManager:
    @pytest.fixture()
    def input_data(self) -> tuple[DataType]:
        data: DataType = {
            "Иванов Иван Иванович": [
                ("математика", 67),
                ("литература", 100),
                ("программирование", 91)
            ],
            "Петров Петр Петрович": [
                ("математика", 81),
                ("химия", 87),
                ("социология", 61)
            ]
        }
        return data

    def test_find_students_with_min_scores(self, input_data: DataType) -> None:
        student_manager = StudentManager(input_data)

        qualified_students = student_manager.find_students_with_min_scores(90,
                                                                           2)
        assert qualified_students == ["Иванов Иван Иванович"]

        qualified_students = student_manager.find_students_with_min_scores(80,
                                                                           2)
        assert qualified_students == ["Иванов Иван Иванович",
                                      "Петров Петр Петрович"]

        qualified_students = student_manager.find_students_with_min_scores(90,
                                                                           3)
        assert qualified_students == []
