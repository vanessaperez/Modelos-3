import random


def random_demand():
    random_number = random.random()
    if 0 <= random_number and random_number <= 0.05:
        return 12
    elif 0.05 < random_number and random_number <= 0.20:
        return 13
    elif 0.20 < random_number and random_number <= 0.45:
        return 14
    elif 0.45 < random_number and random_number <= 0.80:
        return 15
    elif 0.80 < random_number and random_number <= 0.95:
        return 16
    elif 0.95 < random_number and random_number <= 1:
        return 17


def random_delivery_time():
    random_number = random.random()
    if 0 <= random_number and random_number <= 0.20:
        return 1
    elif 0.20 < random_number and random_number <= 0.50:
        return 2
    elif 0.50 < random_number and random_number <= 0.85:
        return 3
    elif 0.85 < random_number and random_number <= 1:
        return 4
