encoding_map = {
    'A':0,
    'E':0,
    'I':0,
    'O':0,
    'U':0,
    'H':0,
    'W':0,
    'Y':0,
    'B':1,
    'F':1,
    'P':1,
    'V':1,
    'C':2,
    'G':2,
    'J':2,
    'K':2,
    'Q':2,
    'S':2,
    'X':2,
    'Z':2,
    'D':3,
    'T':3,
    'L':4,
    'M':5,
    'N':5,
    'R':6
}

def soundex(string):
    string = string.upper()
    print string
    encoding = string[0]
    for i in string[1:]:
        encoding += str(encoding_map[i])
        if encoding[len(encoding) - 1] == encoding[len(encoding) - 2]:
            encoding = encoding[:len(encoding)-1]

    print encoding
    encoding = encoding.split('0')
    encoding = "".join(encoding)
    print encoding[:4]
    return encoding[:4]

print soundex('hermann')
# H655
