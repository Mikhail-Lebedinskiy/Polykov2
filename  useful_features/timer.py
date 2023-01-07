import datetime


arr = {str(i):datetime.datetime.time(0, 0, 0, 0) for i in range(1, 28)}

s = input()
last_time = datetime.datetime.now().time()
while s != 'end':
    last_s = s
    s = input()
    arr[s] += (datetime.datetime.now().time() - last_time)
    last_time = datetime.datetime.now().time()


for key in arr:
    print(f'Номер {key}. Время {arr[key]}')