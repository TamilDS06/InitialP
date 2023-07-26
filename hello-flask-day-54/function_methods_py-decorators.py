## ********Day 54 Start**********
## Functions can have inputs/functionality/output
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

result = calculate(add, 2, 3)
print(result)

##Functions can be nested in other functions

def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()

outer_function()

## Functions can be returned from other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function

inner_function = outer_function()
inner_function()


## Simple Python Decorator Functions
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        function()
        #Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

#With the @ syntactic sugar
@delay_decorator
def say_bye():
    print("Bye")

#Without the @ syntactic sugar
def say_greeting():
    print("How are you?")
decorated_function = delay_decorator(say_greeting)
decorated_function()


def cv(func):
    def wrapper():
        time.sleep(2)
        func()
        func()
    return wrapper

@cv
def poison():
    print("I'm a poison.")

def not_poison():
    print("Im not a poison.")

poison()

wrapper = cv(not_poison)
wrapper()


import time
# current_time = time.time()
# print(current_time)

def speed_calc_decorator(func):
    def wrapper():
        current_time = time.time()
        func()
        run_speed = time.time() - current_time
        print(f'{func.__name__} run speed:{run_speed}')
    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator       
def slow_function():
    for i in range(10000000):
        i * i

slow_function()
fast_function()

### Advanced python Decorators with *args and **kwargs ###
## ********Day 55 Start**********

## Advanced Python Decorator Functions

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)


### Practice-1 ###
class adv_dec_practice_class:

    def __init__(self, number):
        self.number = number

def adv_dec_practice(funcion):
    def wrapper(*args, **kwargs):
        if args[0].number % 2 == 0: funcion(args[0])
        else: pass
    return wrapper

@adv_dec_practice
def func(number_):
    print(f'{number_.number} is even number')

obj = adv_dec_practice_class(6)
func(obj)


### Practice-2 ###
class adv_dec_practice_class:

    def __init__(self, number):
        self.number = number

def adv_dec_practice(funcion):
    def wrapper(*args, **kwargs):
        if kwargs['number_'].number % 2 == 0: funcion(kwargs['number_'])
        else: pass
    return wrapper

obj = adv_dec_practice_class(6)
func(obj)

@adv_dec_practice
def func(number_=obj):
    print(f'{number_.number} is even number')


### coding excercise ###
# Create the logging_decorator() function 👇
def logging_decorator(fucntion):
    def wrapper(*args):
        output = fucntion(*args) # fucntion(args[0], args[1], args[2])
        print(f"You called {fucntion.__name__}{args}\nIt returned: {output}")
    return wrapper
# Use the decorator 👇
@ logging_decorator
def a_function(a, b, c):
    return a+b+c
a_function(1,2,3)