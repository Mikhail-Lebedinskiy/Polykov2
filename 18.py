def f(s):
    for i in range(len(s)-1):
        if s[i] + s[i+1] == "ПР" or s[i] + s[i+1] == "ПТ" or s[i] + s[i+1] == "РП" or s[i] + s[i+1] == "РТ" or s[i] + s[i+1] == "ТР" or s[i] + s[i+1] == "ТП" or s[i] + s[i+1] == "ЕА" or s[i] + s[i+1] == "АЕ":
            return True
    return False