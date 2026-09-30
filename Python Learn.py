import math


def run_hello_world():
    print("Hello World😊😊")
    print("*" * 10)
    print("--------------------------------------------------------------------------")
    x = 1
    y = 2
    unit_price = 3
    print("x =", x)
    print("y =", y)
    print("unit_price =", unit_price)
    print("--------------------------------------------------------------------------")
    student_count = 1000
    rating = 4.99
    is_published = False
    course_name = "Python Programming"
    print(student_count)
    print(course_name)
    print("rating =", rating)
    print("is_published =", is_published)
    print("--------------------------------------------------------------------------")


def run_strings():
    course = "Python Programming"
    message = """
Hi John,

My name is Yeshas Sujith

Blah Blah Blah
"""
    print(message)
    print(len(course))
    print(course[0])
    print(course[-1])
    print(course[0:3])
    print(course[0:])
    print(course[:3])
    print(course[:])
    print("--------------------------------------------------------------------------")

    course = 'Python " Programming'
    print(course)
    course = "Python \" Programming"
    print(course)
    course = "Python \' Programming"
    print(course)
    course = "Python \\ Programming"
    print(course)
    course = "Python \nProgramming"
    print(course)
    print("--------------------------------------------------------------------------")

    first = "Yeshas"
    last = "Sujith"
    full = f"{first} {last}"
    print(full)
    ftype = f"{len(first)} {2 + 2}"
    print(ftype)
    print("--------------------------------------------------------------------------")

    course = "python programming"
    print(course.upper())
    print(course.lower())
    print(course.title())
    print(course)
    course1 = "          python programming"
    print(course1.strip())
    print(course1)
    print(course.find("pro"))
    print(course.replace("p", "j"))
    print("pro" in course)
    print("cool" in course)
    print("swift" not in course)
    print("--------------------------------------------------------------------------")


def run_math_and_input():
    x = 1
    x = 1.1
    x = 1 + 2j
    print(10 + 3)
    print(10 - 3)
    print(10 * 3)
    print(10 / 3)
    print(10 // 3)
    print(10 % 3)
    print(10 ** 3)
    x = 10
    x = x + 3
    x += 3
    print("--------------------------------------------------------------------------")

    print(round(2.9))
    print(abs(-2.9))
    print(math.ceil(2.9))
    print("--------------------------------------------------------------------------")

    x = input("x : ")
    print(type(x))
    y = int(x) + 1
    print(f"x: {x}, y: {y}")
    print("--------------------------------------------------------------------------")


def run_conditions():
    temperature = 15
    if temperature > 30:
        print("It's warm")
        print("Drink water")
    elif temperature > 20:
        print("It's nice")
    else:
        print("It's cold")
    print("Done")
    print("--------------------------------------------------------------------------")

    age = 22
    if age >= 18:
        print("You are Eligible")
    else:
        print("You are not Eligible")

    message = "Eligible " if age >= 18 else "Not Eligible"
    print(message)
    print("--------------------------------------------------------------------------")

    high_income = True
    good_credit = True
    if high_income and good_credit:
        print("Eligible")
    else:
        print("Not Eligible")

    high_income = True
    good_credit = False
    if high_income or good_credit:
        print("Eligible")
    else:
        print("Not Eligible")

    high_income = True
    good_credit = True
    kid = False
    if high_income and good_credit and not kid:
        print("Eligible")
    else:
        print("Not Eligible")
    print("--------------------------------------------------------------------------")

    age = 22
    if age >= 18 and age <= 65:
        print("Eligible")

    if 18 <= age < 65:
        print("Eligible")
    print("--------------------------------------------------------------------------")


def run_loops():
    for number in range(3):
        print("Attempt")

    for number in range(3):
        print("Attempt", number)

    for number in range(3):
        print("Attempt", number + 1)

    for number in range(3):
        print("Attempt", number + 1, (number + 1) * ".")

    for number in range(1, 4):
        print("Attempt", number, number * ".")

    for number in range(1, 10, 2):
        print("Attempt", number, number * ".")

    for number in range(2, 10, 2):
        print("Attempt", number, number * ".")
    print("--------------------------------------------------------------------------")

    successful = True
    for number in range(3):
        print("Attempt")
        if successful:
            print("Successful")
            break
    else:
        print("Attempted but failed")

    successful = False
    for number in range(3):
        print("Attempt")
        if successful:
            print("Successful")
            break
    else:
        print("Attempted but failed")
    print("--------------------------------------------------------------------------")

    for x in range(5):
        for y in range(3):
            print(f"({x}, {y})")
    print("--------------------------------------------------------------------------")

    print(type(5))
    print(type(range(5)))

    for x in "Python":
        print(x)

    for x in [1, 2, 3, 4, 5]:
        print(x)
    print("--------------------------------------------------------------------------")

    number = 100
    while number > 0:
        print(number)
        number //= 2


def run_functions():
    def greet(name):
        return f"Hello, {name}!"

    def add(first_number, second_number=0):
        return first_number + second_number

    def multiply(*numbers):
        total = 1
        for number in numbers:
            total *= number
        return total

    print(greet("Python learner"))
    print("2 + 3 =", add(2, 3))
    print("2 + 0 =", add(2))
    print("2 * 3 * 4 =", multiply(2, 3, 4))
    print("--------------------------------------------------------------------------")


def run_all():
    run_hello_world()
    run_strings()
    run_math_and_input()
    run_conditions()
    run_loops()
    run_functions()


def show_main_menu():
    print("\nWhich topic would you like to explore?")
    print("1) Hello World and basics")
    print("2) Strings")
    print("3) Math, numbers, and input")
    print("4) Conditions")
    print("5) Loops")
    print("6) Functions")
    print("7) Run all")
    print("8) Exit")


def show_sub_menu(topic_name):
    print(f"\nWhich exact program in {topic_name} do you want to run?")
    print("1) Run the main example")
    print("2) Run all examples in this topic")


def main():
    while True:
        show_main_menu()
        choice = input("Enter your topic choice: ").strip().lower()

        if choice in ["8", "exit", "quit"]:
            print("Goodbye!")
            return

        if choice in ["1", "hello", "hello world", "basics"]:
            show_sub_menu("Hello World and basics")
            sub_choice = input(
                "Enter your exact program choice: ").strip().lower()
            if sub_choice in ["1", "main", "example"]:
                run_hello_world()
            elif sub_choice in ["2", "all", "run all"]:
                run_hello_world()
            else:
                print("Invalid choice. Please try again.")
                continue

        elif choice in ["2", "strings", "string"]:
            show_sub_menu("Strings")
            sub_choice = input(
                "Enter your exact program choice: ").strip().lower()
            if sub_choice in ["1", "main", "example"]:
                run_strings()
            elif sub_choice in ["2", "all", "run all"]:
                run_strings()
            else:
                print("Invalid choice. Please try again.")
                continue

        elif choice in ["3", "math", "numbers", "input"]:
            show_sub_menu("Math, numbers, and input")
            sub_choice = input(
                "Enter your exact program choice: ").strip().lower()
            if sub_choice in ["1", "main", "example"]:
                run_math_and_input()
            elif sub_choice in ["2", "all", "run all"]:
                run_math_and_input()
            else:
                print("Invalid choice. Please try again.")
                continue

        elif choice in ["4", "conditions", "if", "ifs"]:
            show_sub_menu("Conditions")
            sub_choice = input(
                "Enter your exact program choice: ").strip().lower()
            if sub_choice in ["1", "main", "example"]:
                run_conditions()
            elif sub_choice in ["2", "all", "run all"]:
                run_conditions()
            else:
                print("Invalid choice. Please try again.")
                continue

        elif choice in ["5", "loops", "loop"]:
            show_sub_menu("Loops")
            sub_choice = input(
                "Enter your exact program choice: ").strip().lower()
            if sub_choice in ["1", "main", "example"]:
                run_loops()
            elif sub_choice in ["2", "all", "run all"]:
                run_loops()
            else:
                print("Invalid choice. Please try again.")
                continue

        elif choice in ["6", "functions", "function"]:
            show_sub_menu("Functions")
            sub_choice = input(
                "Enter your exact program choice: ").strip().lower()
            if sub_choice in ["1", "main", "example", "2", "all", "run all"]:
                run_functions()
            else:
                print("Invalid choice. Please try again.")
                continue

        elif choice in ["7", "all", "run all"]:
            run_all()

        else:
            print("Invalid topic choice. Please choose a number from 1 to 8.")
            continue

        again = input(
            "\nDo you want to choose another program? (y/n): ").strip().lower()
        if again not in ["y", "yes"]:
            print("Goodbye!")
            return


if __name__ == "__main__":
    main()

# command = ""            # This both are the same⬅️↖️
# while True:
#    command = input(">")
#   print("ECHO", command)
#   if command.lower() == "quit":

print("--------------------------------------------------------------------------")
# Exercises ⬇️
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")
print("--------------------------------------------------------------------------")
# Functions ⬇️
# print()
# round()


def greet():  # Greet is a function that takes no arguments and prints a greeting message.
    print("Hi there")
    print("Welcome Aboard")


greet()


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome Aboard")


greet("Yeshas", "Sujith")
greet("John", "Smith")
print("--------------------------------------------------------------------------")
# types of functions ⬇️

# In prgramming, we have two types of functions:
# 1. Perform a task
# 2. Calculate and return a value

round(2.9)  # This is function that calculates and returns a value


# def get_greeting(name):
#    return f"Hi {name}"

# message = get_greeting("Yeshas")         # This program will return the value of the function get_greeting and assign it to the variable message
# file = open("content.txt", "w")          # But there is no file called content.txt in the directory so it will create a new file called content.txt and write the value of the variable message to it.
# file.write(message)                      # So i put it in comments


# def greet(name):
#    print(f"Hi {name}")
#    return "..."


# This will print the return value of the function greet, which is None because the function does not have a return statement
# print(greet("Yeshas"))
# Remember: None is a object that represents the absence of a value.
print("--------------------------------------------------------------------------")
# Keyword Arguments ⬇️


def increment(number, by):
    return number + by


# This will return 3 because the first argument is 2 and the second argument is 1
print(increment(2,  by=1))  # This is more understandable
print("--------------------------------------------------------------------------")
# Default Arguments ⬇️


# This is a default argument which will be used if the second argument is not provided
def increment(number, by=1):
    return number + by


# This will return 3 because the second argument is not provided so the default value of 1 will be used
print(increment(2))
print("--------------------------------------------------------------------------")
# Args, wait, what? ⬇️


def multiply(x, y):  # ⬅️ Parameters are x and y. Arguments are the values that are passed to the function when it is called. In this case, the arguments are 2 and 3.
    return x * y


# This will return 6 because the first argument is 2 and the second argument is 3
multiply(2, 3)
# We cant add 2 more functions because it can only take 2 parameters.


# ⬅️ Parameters are numbers. Arguments are the values that are passed to the function when it is called. In this case, the arguments are 2, 3, 4, 5.
def multiply(*numbers):
    # The numbers are plural so we can have any number of arguments.The * before the parameter name means that the function can take any number of arguments and they will be stored in a tuple called numbers.
    return numbers


multiply(2, 3, 4, 5)

# We can iterate


def multiply(*numbers):
    for number in numbers:
        print(number)


multiply(2, 3, 4, 5)


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
print("--------------------------------------------------------------------")
# Calculating area of a circle
radius = 10                                 # radius of a circle
# two * sign means exponent or power
area_of_circle = 3.14 * radius ** 2
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # Adding unit to the weight
print("----------------------------------------------------------------------------------------")
# Factorals⬇️

fa = int(input(""))
result = math.factorial(fa)
print(result)
