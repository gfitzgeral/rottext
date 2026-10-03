import unittest

from rottext import rot, rot13, unrot


class RottextTest(unittest.TestCase):
    def test_roundtrip(self) -> None:
        self.assertEqual(rot13("Hello, 1"), "Uryyb, 1")
        self.assertEqual(rot13(rot13("Hello")), "Hello")
        self.assertEqual(rot("ab", 1), "bc")
        self.assertEqual(unrot(rot("Hello", 5), 5), "Hello")


if __name__ == "__main__":
    unittest.main()
