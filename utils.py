import random


def random_color():
    return [random.randint(0, 255) for i in range(3)]
