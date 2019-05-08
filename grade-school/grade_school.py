"""Create a simple school."""
from collections import defaultdict


class School(object):
    """Create a simple school."""

    def __init__(self):
        """Initialize."""
        self.students = defaultdict(set)

    def add_student(self, name, grade):
        """Add new student to a grade."""
        self.students[grade].add(name)

    def roster(self):
        """Return all students in the school."""
        return [student for grade in sorted(self.students.keys())
                for student in self.grade(grade)]

    def grade(self, grade_number):
        """Return all students in the grade."""
        return sorted(self.students[grade_number])
