arr = [int(i) for i in '127 127 254 243 543 314 243 254 750 148 314 254 911 243'.split()]
data = {}
for i in arr:
    try:
        data[i] += 1
    except:
        data[i] = 1

answer = 0
for key in data.keys():
    if data[key] >= 2:
        answer += data[key]
        print(key)

print(answer)