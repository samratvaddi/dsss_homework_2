import unittest
from math_quiz import integer, operation, solution

class TestMathQuizFunctions(unittest.TestCase):

    def test_integer(self):
        # Test if random numbers generated are within the range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_operation(self):
        # Test if the random operator is one of the operators
        operators = {'+', '-', '*'}
        for _ in range(1000):  # Test a large number of random values
            rand_operator = operation()
            self.assertTrue(rand_operator in operators)

    def test_solution(self):
        test_cases = [
            (5, 2, '+', 7),
            (3, 4, '-', -1),
            (2, 6, '*', 12),
            # Add more test cases as needed
        ]

        for num1, num2, operator, expected_answer in test_cases:
            calculated_answer = solution(num1, num2, operator)
            self.assertEqual(calculated_answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
