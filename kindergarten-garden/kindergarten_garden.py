"""Determine which plants each child is responsible for."""

STUDENTS = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred",
            "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]


class Garden(object):
    """Determine which plants each child is responsible for."""

    def __init__(self, diagram, students=None):
        """Initialize."""
        self.plant_names = {"V": "Violets", "C": "Clover",
                            "R": "Radishes", "G": "Grass"}
        self.garden = self.make_garden(diagram)
        self.students = sorted(students) if students else STUDENTS

    def plants(self, student):
        """Determine which plants this child is responsible for."""
        try:
            index = self.students.index(student)
            return self.garden[0][2 * index: 2 * index + 2] +\
                self.garden[1][2 * index: 2 * index + 2]
        except ValueError:
            print(f"{student} is not in this class.")

    def make_garden(self, diagram):
        """Create the garden from the diagram."""
        try:
            return [[self.plant_names[plant] for plant in row]
                    for row in diagram.split("\n")]
        except ValueError:
            print("Invalid plant.")
