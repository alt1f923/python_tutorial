import unittest
import questions

class QuestionOneTests(unittest.TestCase):
    def integer_test(self):
        self.assertEqual(questions.add(2, 4), 2 + 4)
    def float_test(self):
        self.assertEqual(questions.add(2.8, 4.2), 2.8 + 4.2)
    def negative_test(self):
        self.assertEqual(questions.add(-3, 2), -3 + 2)

class QuestionTwoTests(unittest.TestCase):
    def integer_test(self):
        self.assertEqual(questions.add_division(2, 4, 6), (2 + 4) / 6)
    def float_test(self):
        self.assertEqual(questions.add_division(2.8, 4.2, 7.0), (2.8 + 4.2) / 7.0)
    def negative_test(self):
        self.assertEqual(questions.add_division(-3, 2, -1), (-3 + 2) / -1)

class QuestionThreeTests(unittest.TestCase):
    def test(self):
        self.assertEqual(questions.fstring("a", "b", 2, 4), "b a6")
        self.assertEqual(questions.fstring("b", "a", 2, 2), "a b4")
    
class QuestionFourTests(unittest.TestCase):
    def test(self):
        self.assertEqual(questions.string_case_concatenation("aB"), "aBabAB")
        self.assertEqual(questions.string_case_concatenation("Ba"), "BabaBA")

class QuestionFiveTests(unittest.TestCase):
    def test(self):
        self.assertEqual(questions.word_square("3"), 9)
        self.assertEqual(questions.word_square("99"), 9801)

class QuestionSixTests(unittest.TestCase):
    def test(self):
        self.assertEqual(questions.float_to_int(9.9999), 9)
        self.assertEqual(questions.float_to_int(1.9999), 9)
        self.assertEqual(questions.float_to_int(9), 9)

class QuestionSevenTests(unittest.TestCase):
    def test(self):
        self.assertEqual(questions.fizzbuzz(15), "fizzbuzz")
        self.assertEqual(questions.fizzbuzz(3), "fizz")
        self.assertEqual(questions.fizzbuzz(5), "buzz")
        self.assertEqual(questions.fizzbuzz(1), 1)