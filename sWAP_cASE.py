def swap_case(s):
    s = list(s)
    for i in range(len(s)):
        j = i
        if s[i] == s[j].upper():
            s[i] = s[i].lower()
        else:
            s[i] = s[i].upper()
    return "".join(s)

if __name__ == '__main__':
