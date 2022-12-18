import unittest
from evens import even_no_ofevens


class TestEvens(unittest.TestCase):
    def test_throws_typeEr_if_passed_value_not_list(self):
        self.assertRaises(TypeError, even_no_ofevens, 4 )
        self.assertEqual(even_no_ofevens([]), False)
        self.assertEqual(even_no_ofevens([1]), False)
        self.assertEqual(even_no_ofevens([2, 4]), True)


if __name__ == '__main__':
    unittest.main()
