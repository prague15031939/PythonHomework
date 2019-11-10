def strFunc(line):
    res = ''
    for i in line:
        if i == '"':
            res += "'"
        elif i == '\'':
            res += '"'
        else:
            res += i
    return res   