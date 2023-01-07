from queue import Queue


queue = Queue()

start_count, border_of_good_mood = [int(i) for i in input().split()]

count_of_good_people = []
current_count_of_good_people = 0
mood_of_lust_people = -1

for mood in [int(i) for i in input().split()]:
    count_of_good_people.append(current_count_of_good_people)
    if mood >= border_of_good_mood:
        current_count_of_good_people += 1
    queue.put(mood)
    mood_of_lust_people = mood


count_of_events = int(input())

number_of_people_left = 0
number_of_good_people_left = 0

for i in range(count_of_events):
    event = [int(i) for i in input().split()]
    if event[0] == 2:
        mood = queue.get()
        number_of_people_left += 1
        if mood >= border_of_good_mood:
            number_of_good_people_left += 1
    elif event[0] == 1:
        queue.put(event[1])
        if mood_of_lust_people >= border_of_good_mood:
            count_of_good_people.append(count_of_good_people[-1] + 1)
        else:
            count_of_good_people.append(count_of_good_people[-1])
        mood_of_lust_people = event[1]
    elif event[0] == 3:
        print(count_of_good_people[event[1] + number_of_people_left] - number_of_good_people_left)







