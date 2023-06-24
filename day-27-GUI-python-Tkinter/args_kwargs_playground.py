# Many Positional args
def add(*args):
    print(args)
    print(type(args))
    total = 0
    for arg in args:
        total += arg
    print(total)


add(1, 2, 3, 4, 5, 6, 7, 8, 9)


# Many key-word args
def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    return n


print(calculate(3, add=0, multiply=2))


class KeyWordCar:

    def __init__(self, **kwargs):
        print(kwargs)
        print(type(kwargs))
        self.make = kwargs.get('make')
        self.color = kwargs.get('color')
        self.seat = kwargs.get('seat')  # it will return None instead of giving key error
        # if the key is not given when initializing the class


my_car = KeyWordCar(make='Maruti', color='White')
print(my_car.make)
print(my_car.color)
print(my_car.seat)  # It will give None.
