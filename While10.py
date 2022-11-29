def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    x=0
    y = 0
    while x<len(s):
        if int(s[x])%2==1:
            y+=int(s[x])
        x+=1
    return y
print(main("589765"))
