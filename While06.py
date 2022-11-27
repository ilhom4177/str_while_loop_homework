def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    counter = 0
    i = 0
    while i < len(s):
        if s[i] != "a" and s[i] != "e" and s[i] != "u" and s[i] != "i" and s[i] != "o":
            counter += 1
        elif s[i] == "A" and s[i] != "E" and s[i] != "U" and s[i] != "I" and s[i] != "O":
            counter += 1
        i += 1
    return counter