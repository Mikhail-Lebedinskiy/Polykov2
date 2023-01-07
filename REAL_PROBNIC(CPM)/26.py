with open('26.txt') as file:
    count_of_box = int(file.readline().strip())
    boxes = []
    for line in file:
        boxes.append(int(line.strip()))

boxes.sort()
blocks = {}
for box in boxes:
    for last_box in sorted(blocks.keys(), reverse=True):
        if box >= last_box + 7:
            pass

