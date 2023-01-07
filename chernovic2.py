waiting_time = -17 * 60 + 28 + 19 * 60 + 30  # время ожидания в минутах
debt_amount = 345  # размер дога в рублях
waiting_fee = 10  # доплата за ожидание
interest_rate = waiting_fee * (365 * 24 * 60 / waiting_time) / waiting_fee * 100  # процентная ставка
print(interest_rate)  # 295280.8988764045
