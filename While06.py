def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    x=0
    y = 0
    while x<len(s):
        if s[x].isalpha():
            if s[x]!='a' and s[x]!='e' and s[x]!='i' and s[x]!='o' and s[x]!='u' and s[x]!='A' and s[x]!='E' and s[x]!='I' and s[x]!='U' and s[x]!='U':
                y += 1
            x+=1
    return y
print(main("CodeschoolUz"))