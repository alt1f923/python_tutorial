import unittest
import questions

class QuestionOneTests(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(questions.add(2, 4), 2 + 4)
    def test_float(self):
        self.assertEqual(questions.add(2.8, 4.2), 2.8 + 4.2)
    def test_negative(self):
        self.assertEqual(questions.add(-3, 2), -3 + 2)

class QuestionTwoTests(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(questions.add_division(2, 4, 6), (2 + 4) / 6)
    def test_float(self):
        self.assertEqual(questions.add_division(2.8, 4.2, 7.0), (2.8 + 4.2) / 7.0)
    def test_negative(self):
        self.assertEqual(questions.add_division(-3, 2, -1), (-3 + 2) / -1)

class QuestionThreeTests(unittest.TestCase):
    def test_floats(self):
        self.assertEqual(questions.float_to_int(9.9999), 9)
        self.assertEqual(questions.float_to_int(1.9999), 9)
    def test_integer(self):
        self.assertEqual(questions.float_to_int(9), 9)

class QuestionFourTests(unittest.TestCase):
    def test_remainders(self):
        self.assertEqual(questions.mod(10, 55), 10)
        self.assertEqual(questions.mod(55, 10), 5)
    def test_no_remainder(self):
        self.assertEqual(questions.mod(81, 9), 0)

class QuestionFiveTests(unittest.TestCase):
    def test_condition_one(self):
        self.assertEqual(questions.piecewise(2), -6)
    def test_condition_two(self):
        self.assertEqual(questions.piecewise(3), 2)
        self.assertEqual(questions.piecewise(4), 9)
        self.assertEqual(questions.piecewise(10), 93)
    def test_condition_three(self):
        self.assertEqual(questions.piecewise(12), 15.0)

if __name__ == '__main__':
    unittest.main()
    
