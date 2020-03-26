"""Count the number of rectangles in a diagram."""

from typing import List, Tuple


def calculate_vector(point: Tuple[int, int], other: Tuple[int, int]) -> List[int]:
    """Calculate the coordinate of the difference vector between two point."""
    return [other[i] - point[i] for i in range(2)]


def check_line_neighbor_points(point: Tuple[int, int], other: Tuple[int, int]) -> bool:
    """Check if a point is on the same line of a given point."""
    vector = calculate_vector(point, other)
    return vector[0] == 0 and vector[1] > 0


def check_column_neighbor_points(
    point: Tuple[int, int], other: Tuple[int, int]
) -> bool:
    """Check if a point is on the same column of a given point."""
    vector = calculate_vector(point, other)
    return vector[0] > 0 and vector[1] == 0


def find_line_neighbor_points(
    point: Tuple[int, int], point_lists: List[Tuple[int, int]]
) -> List[Tuple[int, int]]:
    """Find all the points on the same line of a given point."""
    return [other for other in point_lists if check_line_neighbor_points(point, other)]


def find_column_neighbor_points(
    point: Tuple[int, int], point_lists: List[Tuple[int, int]]
) -> List[Tuple[int, int]]:
    """Find all the points on the same column of a given point."""
    return [
        other for other in point_lists if check_column_neighbor_points(point, other)
    ]


def check_complete_horizontal_line(
    point: Tuple[int, int], other: Tuple[int, int], ascii_diagram: List[str]
) -> bool:
    """Check if a line between two points on the same line is complete."""
    return all(
        [ascii_diagram[point[0]][i] in "-+" for i in range(point[1] + 1, other[1])]
    )


def check_complete_vertical_line(
    point: Tuple[int, int], other: Tuple[int, int], ascii_diagram: List[str]
) -> bool:
    """Check if a line between two points on the same column is complete."""
    return all(
        [ascii_diagram[i][point[1]] in "|+" for i in range(point[0] + 1, other[0])]
    )


def rectangles(ascii_diagram: List[str]) -> None:
    """Count the number of rectangles in a diagram."""
    point_lists = [
        (i, j)
        for i, line in enumerate(ascii_diagram)
        for j, char in enumerate(line)
        if ascii_diagram[i][j] == "+"
    ]
    number = 0
    for point in point_lists:
        line_neighbor_points = find_line_neighbor_points(point, point_lists)
        column_neighbor_points = find_column_neighbor_points(point, point_lists)
        for line_point in line_neighbor_points:
            for column_point in column_neighbor_points:
                if not (
                    check_complete_horizontal_line(point, line_point, ascii_diagram)
                    and check_complete_vertical_line(point, column_point, ascii_diagram)
                ):
                    break
                fourth_point = (column_point[0], line_point[1])
                if ascii_diagram[fourth_point[0]][fourth_point[1]] == "+":
                    if check_complete_horizontal_line(
                        column_point, fourth_point, ascii_diagram
                    ) and check_complete_vertical_line(
                        line_point, fourth_point, ascii_diagram
                    ):
                        number = number + 1
    return number
