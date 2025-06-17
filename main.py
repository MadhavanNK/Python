
# Name ="madhavan"
# age ="23"
# role ="Software engineer" 

# print("i am " +Name +" working as a " +role +" may age is "+age)

# Name ="madhavan"
# age =23
# role ="Software engineer" 

# print(f"I am {Name}, working as a {role}, my age is {age}")

# a="Good"
# b="Morning"
# c=a+" "+b
# print(c)


# a="Good"
# b="Morning"
# c=f"hi {a} {b}"
# print(c)

# a = 10
# b = 3

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a//b)
# print(a**b)


# import math


# print("Square root of 25:", math.sqrt(25))

# print("2 to the power 3:", math.pow(2, 3))

# print("Floor of 3.7:", math.floor(3.7))

# print("Ceil of 3.7:", math.ceil(3.7))

# print("Absolute of -7:", math.fabs(-7))

# print("Factorial of 5:", math.factorial(5))

# print("Pi value:", math.pi)

# print("Euler's number:", math.e)



# import random


# print("Random float:", random.random())


# print("Random integer:", random.randint(1, 100))


# print("Random float between 5 and 10:", random.uniform(5, 10)) 


# fruits = ['apple', 'banana', 'cherry', 'orange']
# print("Random fruit:", random.choice(fruits))


# print("Sample 2 fruits:", random.sample(fruits, 2))


# print("Choices 3 fruits (with repeat):", random.choices(fruits, k=3))


# numbers = [1, 2, 3, 4, 5]
# random.shuffle(numbers)
# print("Shuffled numbers:", numbers)



# x = 10

# if x > 5:
#     print("x is greater than 5")


# x = 3

# if x > 5:
#     print("x is greater than 5")
# else:
#     print("x is 5 or less")


# x = 3

# if x > 10:
#     print("x is greater than 10")
# elif x > 5:
#     print("x is greater than 5 but less than or equal to 10")
# else:
#     print("x is 5 or less")


# age = 20

# result = "Adult" if age >= 18 else "Minor"
# print(result)

# x = 10

# if x > 5:
#     if x < 15:
#         print("x is between 5 and 15")




# def first():
#     print("Hello!")
# first()



# def first(name):
#     print("Hello!",name)
# first("madhavan")



# def first(name, age):
#     print(name, "is", age, "years old")

# first(age=23, name="madhavan")




# def square(x):
#     return x * x

# result = square(4)
# print(result)  



# def first(name="Guest"):
#     print(f"Hello, {name}")

# first()         
# first("madhavan")  




# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Cannot divide by zero"
#     except TypeError:
#         return "Inputs must be numbers"
#     finally:
#         print("Divide function was called")

# print(divide(10, 0))    
# print(divide(10, 'a'))  
# print(divide(10, 2))    




def get_element():
    try:
        numbers = [10, 20, 30, 40]
        index = int(input("Enter the index (0 to 3): "))
        print("Element at index", index, "is", numbers[index])
    except ValueError:
        print("Please enter a valid number.")
    except IndexError:
        print("Index out of range. Please enter between 0 and 3.")
    finally:
        print("Finished trying to get element.")


get_element()



