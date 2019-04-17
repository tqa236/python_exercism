"""Create a simple school."""


class School(object):
    """Create a simple school."""

    def __init__(self):
        """Initialize."""
        self.students = {}

    def add_student(self, name, grade):
        """Add new student to a grade."""
        self.students.setdefault(grade, set()).add(name)

    def roster(self):
        """Return all students in the school."""
        return [student for grade in sorted(self.students.keys())
                for student in sorted(self.students[grade])]

    def grade(self, grade_number):
        """Return all students in the grade."""
        return sorted(self.students.setdefault(grade_number, []))
