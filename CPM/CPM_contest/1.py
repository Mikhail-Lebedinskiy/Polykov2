N = int(input())
M = int(input())
number_of_stops = (N - 1) // M
time_to_stops = (1 + number_of_stops) * number_of_stops // 2


time_to_travel = N
all_time = time_to_travel + time_to_stops
print(all_time)