import unittest
from math_quiz import integer, operation, solution

class TestMathGame(unittest.TestCase):

    def test_integer(self):
        min_val = 1
        max_val = 10
        for _ in range(1000):  
            rand_num = integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_operation(self):
        valid_operators = {'+', '-', '*'}
        for _ in range(1000):  
            operator = operation()
            self.assertIn(operator, valid_operators)

    def test_solution(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 3, '-', '10 - 3', 7),
            (4, 5, '*', '4 * 5', 20),
            (20, 4, '/', '20 / 4', 5),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            _, result_answer = solution(num1, num2, operator)  
            self.assertEqual(result_answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
