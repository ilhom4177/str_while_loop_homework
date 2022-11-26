def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    counter = 0
    i = 0
    while i < len(s):
        if s[i].isdigit():
            counter += 1
        i += 1
    return counter