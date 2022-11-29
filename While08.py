def main(s):
    """
    A string of numbers is given. Find how many odd numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    n=0
    while i<len(s):
        if int(s[i])%2==1:
            n=n+1
        i=i+1
    return n
print(main('1234567'))