import re

# Allowed letters (no I, O, Q)
ALLOWED_LETTERS = "ABCDEFGHJKLMNPRSTUVWXYZ"

# Token specification
TOKEN_SPEC = [
    ("LETTER", r"[{}]".format(ALLOWED_LETTERS)),
    ("DIGIT",  r"[0-9]"),
    ("DASH",   r"-"),
]

token_regex = "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPEC)

def lexer(text):
    tokens = []
    for match in re.finditer(token_regex, text):
        kind = match.lastgroup
        value = match.group()
        tokens.append((kind, value))
    return tokens
