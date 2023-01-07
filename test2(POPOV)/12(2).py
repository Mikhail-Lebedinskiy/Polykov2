i = "1" * 170 + "3" * 100 + "2" * 7
a = "11"


while a in i:
    i = i.replace("112", "4", 1)
    i = i.replace("113", "2", 1)
    i = i.replace("42", "3", 1)
    i = i.replace("43", "1", 1)
print(i)