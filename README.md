# rottext

ROT13. Letters rotate by 13. Digits, spaces, and punctuation are unchanged. Applying it twice returns the original text.

```python
from rottext import rot13, rot, unrot

rot13("Hello")
rot("ab", 1)  # "bc"
unrot(rot("Hello", 5), 5)  # "Hello"
```

```bash
python -m unittest test_rottext.py
```

MIT
