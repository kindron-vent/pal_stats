# objec - understand the importance of scope
# lear LEGB rule for scope resolution
"""
x = 2
print(x)

x = 3
print(x)
print(sum(x + 2))
"""
"""
# local scope-inside the function body
# global scope - codes outside the function body
x = "Hello, World"
def func():
    x = 2
    print(f"Inside 'func', x has the value {x}")  

func()
print(f"Outside 'func' , x has the value {x}")
"""


# scope resolution
# scope have a hierarchy
x = 5

def outer_func():
    y = 3

    def inner_func():
        z = x + y
        return z
    
    return inner_func()
print(outer_func())


# break rules
"""
total = 0
def add_to_total(n):
    total = total + n
add_to_total(5)
print(total) # produce error message
"""

# total = 0

# def add_to_total(n):
#     global total
#     total = total + n

# add_to_total(5)
# print(total)

# creating inner Functions
# has ability to access enclosed objects/variables
"""
def outer_func():
    def inner_func():
        print("Hello, World")
    inner_func()
print(outer_func())
"""
"""
def outer_func(who):
    def inner_func():
        print(f"Hello,{who}")
    inner_func()

outer_func("World!")

# factorial numbers
def factorial(number):
    # validate input
    if not isinstance(number, int):
        raise TypeError("Sorry. 'number' must be an integer.")
    if number < 0:
        raise ValueError("Sorry. 'number' must be zero or postive.")
    # Calculate the factorial of number
    def inner_factorial(number):
        if number <= 1:
            return 1
        return inner_factorial(number - 1) * number
    return inner_factorial(number)

print(factorial(5))
"""

"""
# using inner Functions: Basics 
# encapsulation and hide functions from external access
# hide/protect from global scope

def increment(number):
    def inner_increment():
        return number + 1
    return inner_increment()

print(increment(300))
"""
"""
# Random tests
list = ['Python', 'Developers']
result = [i for i in list if len(i)>6]
print(*result)
"""

def outer_fn():
    def inner_fn():
        print("Hello inside!")
    print("Hello outside!")
    inner_fn()

outer_fn()

def mug(stuff):
    def inside():
        print(f"Yummy {stuff}")
    inside()
mug("coffee")
    






