import unittest


from math_operation import addition_operation, subtraction_operation


class TestOperations(unittest.TestCase):
    def test_adition_operatin(self):
        math_addition_result = addition_operation(num_1=5, num_2=10)
        self.assertEqual(math_addition_result, 15)


if __name__ == '__main__':
    unittest.main()
    assert subtraction_operation(num_1=10, num_2=10) == 0
