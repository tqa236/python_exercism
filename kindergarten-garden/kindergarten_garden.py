"""Determine which plants each child is responsible for."""

STUDENTS = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred",
            "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
PLANT_NAMES = {"V": "Violets", "C": "Clover",
               "R": "Radishes", "G": "Grass"}


class Garden(object):
    """Determine which plants each child is responsible for."""

    def __init__(self, diagram, students=None):
        """Initialize."""
        try:
            self.garden = [[PLANT_NAMES[plant] for plant in row]
                           for row in diagram.split("\n")]
        except ValueError:
            print("Invalid plant.")

        self.students = sorted(students) if students else STUDENTS

    def plants(self, student):
        """Determine which plants this child is responsible for."""
        try:
            start = self.students.index(student) * 2
            end = start + 2
            return [plant for row in self.garden for plant in row[start: end]]
        except ValueError:
            print(f"{student} is not in this class.")
