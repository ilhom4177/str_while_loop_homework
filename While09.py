def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    x=0
    k=0
    while x<len(s):
        k+=int(s[x])
        x+=1
    return k

print(main("12"))