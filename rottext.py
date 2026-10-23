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


def matches_rot(text: str, other: str, steps: int = 13) -> bool:
    return rot(text, steps) == other


def letter_count(text: str) -> int:
    return sum(1 for char in text if ("a" <= char <= "z") or ("A" <= char <= "Z"))


def keeps(text: str) -> str:
    return "".join(
        char for char in text if not (("a" <= char <= "z") or ("A" <= char <= "Z"))
    )


def moved(text: str, steps: int = 13) -> int:
    shifted = rot(text, steps)
    return sum(1 for left, right in zip(text, shifted) if left != right)


def unchanged(text: str, steps: int = 13) -> bool:
    return rot(text, steps) == text


def shifted(text: str, steps: int = 13) -> str:
    moved_text = rot(text, steps)
    return "".join(right for left, right in zip(text, moved_text) if left != right)


def kept_count(text: str) -> int:
    return len(keeps(text))


def all_kept(text: str) -> bool:
    return kept_count(text) == len(text)
