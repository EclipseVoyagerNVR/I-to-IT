def srtings(string):
    s = ''
    for i in range(len(string)):
        s += string[i] + '=>' + str(ord(string[i])) + ' '
    return s