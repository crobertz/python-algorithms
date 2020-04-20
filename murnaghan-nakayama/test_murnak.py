import unittest
import murnak


class MurNakTest(unittest.TestCase):

    def test_charval(self):
        self.assertEqual(murnak.character([], []), 1)
        self.assertEqual(murnak.character([1], [1]), 1)
        self.assertEqual(murnak.character([5, 2, 1], [3, 3, 1, 1]), -2)
        self.assertEqual(murnak.character([3, 3, 1, 1], [5, 2, 1]), 1)
        self.assertEqual(murnak.character([3, 2, 1], [1, 1, 1, 1, 1, 1]), 16)
        self.assertEqual(murnak.character([3, 3, 3], [8, 1]), 0)
        self.assertEqual(murnak.character([3, 3, 3], [4, 3, 2]), -2)
        with self.assertRaises(SystemExit) as cm:
            murnak.character([3, 2, 1], [2, 2])
            self.assertEqual(cm.exception, "Need two partitions of same integer")

    def test_partition_to_list(self):
        self.assertEqual(murnak.partition_to_list([3, 2]), [[1, 2, 3], [4, 5]])
        self.assertEqual(murnak.partition_to_list([]), [])
        self.assertEqual(murnak.partition_to_list([5]), [[1, 2, 3, 4, 5]])

    def test_make_youngdiag(self):
        self.assertEqual(murnak.make_youngdiag([]), {})
        self.assertEqual(murnak.make_youngdiag([2, 1]), {1: {'r': 2, 'd': 3, 'l': None, 'u': None}, 2: {'r': None, 'd': None, 'l': 1, 'u': None}, 3: {'r': None, 'd': None, 'l': None, 'u': 1}})
        self.assertEqual(murnak.make_youngdiag([3]), {1: {'r': 2, 'd': None, 'l': None, 'u': None}, 2: {'r': 3, 'd': None, 'l': 1, 'u': None}, 3: {'r': None, 'd': None, 'l': 2, 'u': None}})
        self.assertEqual(murnak.make_youngdiag([1, 1, 1]), {1: {'r': None, 'd': 2, 'l': None, 'u': None}, 2: {'r': None, 'd': 3, 'l': None, 'u': 1}, 3: {'r': None, 'd': None, 'l': None, 'u': 2}})


if __name__ == '__main__':
    unittest.main()
