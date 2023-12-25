from collections import defaultdict


class School(object):
    def __init__(self) -> None:
        self.students = defaultdict(set)
        self.added_students = []
        self.student_names = set()

    def add_student(self, name: str, grade: int) -> None:
        if name in self.student_names:
            self.added_students.append(False)
            return
        self.students[grade].add(name)
        self.added_students.append(True)
        self.student_names.add(name)

    def roster(self) -> list[str]:
        return [
            student
            for grade in sorted(self.students.keys())
            for student in self.grade(grade)
        ]

    def grade(self, grade_number: int) -> list[str]:
        return sorted(self.students[grade_number])

    def added(self):
        return self.added_students
