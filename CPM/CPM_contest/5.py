def max_number_of_water_after_3_days(number_of_stations, number_of_drones):
    number_of_water = 0
    number_of_water, number_of_drones = number_of_water + number_of_drones, number_of_drones + number_of_stations
    number_of_water, number_of_drones = number_of_water + number_of_drones, number_of_drones + number_of_stations
    number_of_water, number_of_drones = number_of_water + number_of_drones, number_of_drones + number_of_stations
    return number_of_water


def main():
    N = int(input())
    number_of_stations = 1
    number_of_drones = 0
    number_of_days = 0
    while True:
        if max_number_of_water_after_3_days(number_of_stations, number_of_drones) >= N:
            number_of_water = 0
            number_of_water, number_of_drones = number_of_water + number_of_drones, number_of_drones + number_of_stations
            if number_of_water >= N:
                return number_of_days + 1
            number_of_water, number_of_drones = number_of_water + number_of_drones, number_of_drones + number_of_stations
            if number_of_water >= N:
                return number_of_days + 2
            return number_of_days + 3
        number_of_stations += number_of_stations
        number_of_days += 1


print(main())