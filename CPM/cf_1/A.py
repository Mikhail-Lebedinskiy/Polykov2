count_of_tests = int(input())
drone_speed = int(input())
max_speed = int(input())

max_offenses = 0
min_offenses = 0

for _ in range(count_of_tests):
    car_speed = int(input())
    if car_speed + drone_speed > max_speed:
        max_offenses += 1
    if abs(car_speed - drone_speed) > max_speed:
        min_offenses += 1

print(min_offenses, max_offenses)