import unittest
import murnak


class MurNakTest(unittest.TestCase):

    def test_charval(self):
        self.assertEqual(murnak.character([1], [1]), 1)


if __name__ == '__main__':
    unittest.main()