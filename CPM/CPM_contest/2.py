number_of_dates = int(input())
last_h, last_m, last_s = -1, -1, -1
count_of_days = 1
for i in range(number_of_dates):
    h, m, s = [int(i) for i in input().split(':')]
    if h < last_h:
        count_of_days += 1
    elif h == last_h and m < last_m:
        count_of_days += 1
    elif h == last_h and m == last_m and s <= last_s:
        count_of_days += 1
    last_h, last_m, last_s = h, m, s

print(count_of_days)

