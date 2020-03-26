"""Create a simple school."""
from collections import defaultdict
from typing import List


class School(object):
    """Create a simple school."""

    def __init__(self) -> None:
        """Initialize."""
        self.students = defaultdict(set)

    def add_student(self, name: str, grade: int) -> None:
        """Add new student to a grade."""
        self.students[grade].add(name)

    def roster(self) -> List[str]:
        """Return all students in the school."""
        return [
            student
            for grade in sorted(self.students.keys())
            for student in self.grade(grade)
        ]

    def grade(self, grade_number: int) -> List[str]:
        """Return all students in the grade."""
        return sorted(self.students[grade_number])
