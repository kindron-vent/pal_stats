# 4.5 - Challenge: Pick Apart Your User's Input
# Solution to code challenge


# Return the upper-case first letter entered by the user

# user_input = input("Tell me your password: ")
# first_letter = user_input[0]
# print("The first letter you entered was: " + first_letter.upper())

#using strings with arithmetic operators
# num = "2"
# num + num
# print(num + num)
# print(num * 3)
# print(3*num)
# num = input("Enter a number to be doubled: ")
# doubled_num = float(num) * 2
# print(doubled_num)
#convert a string to a number
# use: int() for integer and float() for floating point number

# int("12")
# print(float("12"))

#converting Numbers to strings
# num_pancakes = 10
# "I am going to eat" + str(num_pancakes) + " pancakes."

#chapter 4.6 exercise
#exercise 1 store an integer as a string
# my_integer_string = "22"

# convert the 'integer' string into an int object using int()
# multiply the integer by 10 and display the results
# print(int(my_integer_string) * 10)

# Exercise 2
# Store a floating-point number as a string
# my_float_string = "500.01"
# Convert the 'float' string into a number using float()
# Multiply the number by 5 and display the result
# print(float(my_float_string) * 5)

#exe 3 create a string and an int object, then display them together
# my_string = "data"
# my_int = 23
# print(my_string + str(my_int))


#Exercise 4
#Get two numbers from the user, multiply them and display the result
# a = input("Enter a number: ")
# b = input("Enter another number: ")
# product = float(a) * float(b)
# print("The product of " + a + " and " + b + " is " + str(product) + " . ")


#4.7 streamlining print statements
# name = "Zaphod"
# heads = 2
# arms = 3
#string interpolation- inserts some variables into specific location in a string
# print(name + " has " + str(heads) + " heads and " + str(arms) + " arms")
#   another way of interpolating strings: formatted string literals, more commonly
# known as f-strings
# print(f"{name} has {heads} heads and {arms} arms") # f for f-string
#Variable names surrounded by curly braces ({}) are replaced by
# their corresponding values without using str()
#Youcanalsoinsert Python expressions between the curly braces
# n = 3
# m = 4
# print(f"{n} times {m} is {n*m}")

#Review exercise 4.7
# create a float object named weight with a value 0.2
# weight = float(0.2)
# create a string object named animal with a value newt
# animal = "newt"
# print the following string using string concatenation
# print(str(weight) + "kg is the weight of the" + animal + ".")

# Find a string in a string
# .find()  find the location of one string in another string 
# phrase = "the surprise is in here somewhere"
# print(phrase.find("surprise"))
# print(phrase.find("GRDSOE"))
# print(phrase.find("SURPRISE"))

# if a substring appears more than once, then .find() returns the index of the first
# my_story = "i put a string in your string"
# print(my_story.find("string"))
# .find() only accepts a string as its inputs
#  finding an integer use .find() as a string
# my_number = "My number is 555-5555"
# print(my_number.find("5"))
# .replace() replaces each instance of a substring with another string
# my_strory_0 = "I'm telling you the truth; nothing but the truth!"
# print(my_strory_0.replace("the truth", "lies"))
# ex_48 = "AAA"
# print(ex_48.find("a"))
# som_stmt = "Somebody said something to Samantha."
# print(som_stmt.replace("s", "x"))
# my_input = input("Type something: ")
# print(my_input.find("X"))

my_text = input("Enter some text: ")
my_text = my_text.replace("a","4")
my_text = my_text.replace("b", "8")
my_text = my_text.replace("e","3")
my_text = my_text.replace("l", "1")
my_text = my_text.replace("o", "0")
my_text = my_text.replace("s", "5")
my_text = my_text.replace("t", "7")
print(my_text)

# Get user input
text = input("Enter some text: ")

# Convert to leetspeak using chained .replace() calls
leetspeak = (text.replace('a', '4')
                 .replace('b', '8')
                 .replace('e', '3')
                 .replace('l', '1')
                 .replace('o', '0')
                 .replace('s', '5')
                 .replace('t', '7'))

# Display the result
print(leetspeak)


