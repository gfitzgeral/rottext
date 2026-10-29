import unittest

from rottext import all_kept, keeps, kept_count, letter_count, matches_rot, moved, none_kept, rot, rot13, shifted, unchanged, unrot, some_kept


class RottextTest(unittest.TestCase):
    def test_roundtrip(self) -> None:
        self.assertEqual(rot13("Hello, 1"), "Uryyb, 1")
        self.assertEqual(rot13(rot13("Hello")), "Hello")
        self.assertEqual(rot("ab", 1), "bc")
        self.assertEqual(unrot(rot("Hello", 5), 5), "Hello")
        self.assertTrue(matches_rot("ab", "bc", 1))
        self.assertFalse(matches_rot("ab", "ab", 1))
        self.assertEqual(letter_count("Hello, 1"), 5)
        self.assertEqual(letter_count("123"), 0)
        self.assertEqual(keeps("Hello, 1"), ", 1")
        self.assertEqual(moved("Hello, 1"), 5)
        self.assertTrue(unchanged("Hello", 26))
        self.assertFalse(unchanged("Hello", 13))
        self.assertEqual(shifted("ab", 1), "bc")
        self.assertEqual(shifted("1", 1), "")
        self.assertEqual(kept_count("Hello, 1"), 3)
        self.assertTrue(all_kept("123"))
        self.assertFalse(all_kept("Hello, 1"))
        self.assertTrue(none_kept("Hello"))
        self.assertFalse(none_kept("Hello, 1"))


        self.assertTrue(some_kept("Hello, 1"))
        self.assertFalse(some_kept("Hello"))

if __name__ == "__main__":
    unittest.main()
