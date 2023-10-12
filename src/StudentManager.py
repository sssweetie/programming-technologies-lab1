class StudentManager:
    def __init__(self, students):
        self.students = students

    def find_students_with_min_scores(self, min_score, min_subjects):
        qualified_students = []

        for name, scores in self.students.items():
            count_subjects_with_min_score = sum(score >= min_score
                                                for subject, score in scores)
            if count_subjects_with_min_score >= min_subjects:
                qualified_students.append(name)

        return qualified_students

    def find_and_print_qualified_student(self, min_score, min_subjects):
        qualified_students = self.find_students_with_min_scores(min_score,
                                                                min_subjects)

        if qualified_students:
            # Выведем первого попавшегося студента, удовлетворяющего условию
            print(f"Первый студент, удовлетворяющий условию
                  ({min_score} баллов минимум
                   по {min_subjects} дисциплинам): ")
            print(qualified_students[0])
        else:
            print(f"Нет студентов, удовлетворяющих условиям.")
