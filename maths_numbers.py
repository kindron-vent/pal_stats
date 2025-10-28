# integers and floating-point numbers
# integers ( a whole number with no decimal)
# print(type(10))
# num = 25
# print(type(int("25")))
# # you cannot use commas to group digits
# # but you can use underscore (_)
# num1 = 1000000
# print(num1)
# num2 = 1_000_000
# print(num2)

# # Floating-Point Numbers
# # it is a number with a decimal point
# print(type(2.5))
# float can be created from floating-point literals
# or by converting a string to a float with float()
# print(float("1.25"))
# print(1000000.0)
# print(1_000_000_000_000.00)
# using E notation to create a float literal
# Y = 1e6
# print(Y)
# print(1e-4)
# print(2e17) # The + sign indicates that the exponent 17 is a positive number
# floats have a maximum size
# upon reaching max, python returns a special float value, inf
# n = 2e400
# # print(n)
# print(type(n))

# ex 5.1
"""
num_1 = 25000000
num_2 = 25_000_000
print(num_1)
print(num_2)
num_e = 17.5e4
print(num_e)
nija1 = 2e409
print(nija1)
nija2 = -2e410
print(nija2) 
"""

# Arithmetic Operators and Expressions
# integer division using // floor division operator
# // is equivalent of modulo %% in R
print(9//3)
print(8//5)

# exponents
# you can raise a number to a power using the ** operators
bedan = 4**3
print(bedan)
# exponents don't have to be integers. They can also be float
benar0 = 3**1.3
print(benar0)