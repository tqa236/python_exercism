import unittest

from hypothesis import given, settings
from hypothesis.strategies import integers, lists

from book_store_hard import optimal_cost, optimal_cost1

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.4.0


class BookStoreTest(unittest.TestCase):
    @given(
        list1=lists(integers(min_value=0, max_value=3), min_size=5, max_size=5),
        list2=lists(integers(min_value=1, max_value=2), min_size=4, max_size=4),
    )
    @settings(deadline=None)
    def test_two_methods(self, list1, list2):
        self.assertEqual(
            optimal_cost(list1, [0] + sorted(list2)),
            optimal_cost1(list1, [0] + sorted(list2)),
        )

    # def test_unit_two_methods(self):
    #     list1 = [0, 0, 0, 1, 2]
    #     list2 = [1, 1, 1, 1]
    #     self.assertEqual(
    #         optimal_cost(list1, [0] + sorted(list2)),
    #         optimal_cost1(list1, [0] + sorted(list2)),
    #     )


if __name__ == "__main__":
    unittest.main()
