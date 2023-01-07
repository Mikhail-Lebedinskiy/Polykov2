len_of_road, len_of_alg = [int(i) for i in input().split()]

road = input()

max_left, max_right = 0, 0
cur_left, cur_right = 0, 0
for command in input():
    if command == 'L':
        cur_left += 1
        cur_right -= 1
    else:
        cur_left -= 1
        cur_right += 1

    max_left = max(max_left, cur_left)
    max_right = max(max_right, cur_right)

cur_droids_max_right_cords = set()
cur_droids = dict()
all_droids = set()
bed_droids = set()

for i, block in enumerate(road):
    if block == '#':
        for droid_cord in cur_droids.values():
            bed_droids.add(droid_cord + 1)
        cur_droids = {}
        cur_droids_max_right_cords = set()
    if block == 'D':
        all_droids.add(i + 1)
        cur_droids[i + max_right] = i
        cur_droids_max_right_cords.add(i + max_right)
    if i in cur_droids_max_right_cords:
        cur_droids_max_right_cords.remove(i)
        cur_droids.pop(i)

for droid_cord in cur_droids.values():
    bed_droids.add(droid_cord + 1)

cur_droids_max_left_cords = set()
cur_droids = dict()
for i, block in enumerate(road[::-1]):
    if block == '#':
        for droid_cord in cur_droids.values():
            bed_droids.add(len_of_road - droid_cord)
        cur_droids = {}
        cur_droids_max_left_cords = set()
    if block == 'D':
        cur_droids[i + max_left] = i
        cur_droids_max_left_cords.add(i + max_left)
    if i in cur_droids_max_left_cords:
        cur_droids_max_left_cords.remove(i)
        cur_droids.pop(i)

for droid_cord in cur_droids.values():
    bed_droids.add(len_of_road - droid_cord)


good_droids = all_droids - bed_droids
print(len(good_droids))
print(*sorted(list(good_droids)))

