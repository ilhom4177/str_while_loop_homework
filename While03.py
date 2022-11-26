import string 
def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    counter = 0
    i = 0
    while i < len(s):
        if not s[i].isdigit() and not s[i].isalpha():
            counter += 1
        i += 1
    return counter
print(main('#hashtag@$'))