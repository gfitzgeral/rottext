"""ROT13 for letters. Digits and punctuation stay put."""
from __future__ import annotations


def rot(text: str, steps: int = 13) -> str:
    shift = steps % 26
    out = []
    for char in text:
        if "a" <= char <= "z":
            out.append(chr((ord(char) - 97 + shift) % 26 + 97))
        elif "A" <= char <= "Z":
            out.append(chr((ord(char) - 65 + shift) % 26 + 65))
        else:
            out.append(char)
    return "".join(out)


def unrot(text: str, steps: int = 13) -> str:
    return rot(text, -steps)


def rot13(text: str) -> str:
    return rot(text, 13)
