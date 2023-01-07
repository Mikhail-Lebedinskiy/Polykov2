count_of_boys = int(input())
count_of_girls = int(input())
time_boy = int(input())
time_girl = int(input())
time_universal = int(input())
max_count_of_universal = int(input())


if time_boy < time_universal and time_girl < time_universal:
    print(time_boy * count_of_boys + time_girl * count_of_girls)
elif time_boy < time_universal < time_girl:
    c = count_of_girls - max_count_of_universal
    if c > 0:
        print(time_boy * count_of_boys + time_girl * c + time_universal * max_count_of_universal)
    else:
        print(time_boy * count_of_boys + time_universal * count_of_girls)
elif time_boy > time_universal > time_girl:
    c = count_of_boys - max_count_of_universal
    if c > 0:
        print(time_girl * count_of_girls + time_boy * c + time_universal * max_count_of_universal)
    else:
        print(time_girl * count_of_girls + time_universal * count_of_boys)
elif time_boy > time_universal and time_girl > time_universal:
    if time_boy > time_girl:
        c = count_of_boys - max_count_of_universal
        if c > 0:
            print(time_girl * count_of_girls + time_boy * c + time_universal * max_count_of_universal)
        else:
            x = count_of_girls + c
            if x > 0:
                print(time_universal * count_of_boys + time_universal * abs(c) + time_girl * x)
            else:
                print(time_universal * (count_of_boys + count_of_girls))
    else:
        c = count_of_girls - max_count_of_universal
        if c > 0:
            print(time_boy * count_of_boys + time_girl * c + time_universal * max_count_of_universal)
        else:
            x = count_of_boys + c
            if x > 0:
                print(time_universal * count_of_girls + time_universal * abs(c) + time_boy * x)
            else:
                print(time_universal * (count_of_girls + count_of_boys))
