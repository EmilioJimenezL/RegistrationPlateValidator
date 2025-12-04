def parse_license(tokens):
    # Expected sequence: LETTER LETTER LETTER DASH DIGIT DIGIT DASH DIGIT DIGIT
    expected = ["LETTER", "LETTER", "LETTER", "DASH",
                "DIGIT", "DIGIT", "DASH", "DIGIT", "DIGIT"]

    if len(tokens) != len(expected):
        return False

    for token, exp in zip(tokens, expected):
        if token[0] != exp:
            return False
    return True
