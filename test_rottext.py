import unittest

from rottext import rot13


class RottextTest(unittest.TestCase):
    def test_roundtrip(self) -> None:
        self.assertEqual(rot13("Hello, 1"), "Uryyb, 1")
        self.assertEqual(rot13(rot13("Hello")), "Hello")


if __name__ == "__main__":
    unittest.main()
