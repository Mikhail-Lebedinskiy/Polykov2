price_of_purchase, price_of_receipt = [int(i) for i in input().split()]

number_of_payments = int(input())


calendar = dict()
for i in range(number_of_payments):
    number_of_money, time = [int(i) for i in input().split()]
    try:
        calendar[time]['payments'] += number_of_money
    except KeyError:
        calendar[time] = {'payments': number_of_money, 'purchase': {'count': 0, 'time_receipt': -1},
                          'count_of_receipt': 0}

for i in range(int(input())):
    time_purchase, time_receipt = [int(i) for i in input().split()]
    try:
        calendar[time_purchase]['purchase'] = {'count': 1, 'time_receipt': time_receipt}
    except KeyError:
        calendar[time_purchase] = {'payments': 0, 'purchase': {'count': 1, 'time_receipt': time_receipt},
                                   'count_of_receipt': 0}
    try:
        calendar[time_receipt] = calendar[time_receipt]
    except KeyError:
        calendar[time_receipt] = {'payments': 0, 'purchase': {'count': 0, 'time_receipt': -1},
                                   'count_of_receipt': 0}


number_of_purchased = 0
current_number_of_money = 0
for time in sorted(calendar.keys()):
    current_number_of_money += calendar[time]['payments']
    if calendar[time]['purchase']['count'] == 1:
        if current_number_of_money >= price_of_purchase:
            current_number_of_money -= price_of_purchase
            number_of_purchased += 1
        else:
            try:
                calendar[calendar[time]['purchase']['time_receipt']]['count_of_receipt'] = 1
            except KeyError:
                calendar[calendar[time]['purchase']['time_receipt']] = {'payments': 0, 'purchase':
                    {'count': 0, 'time_receipt': -1}, 'count_of_receipt': 1}
    else:
        if calendar[time]['count_of_receipt'] == 1:
            if current_number_of_money >= price_of_receipt:
                current_number_of_money -= price_of_receipt
                number_of_purchased += 1
print(number_of_purchased)

