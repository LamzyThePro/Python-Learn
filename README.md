# 🐍 Python Learn

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Level](https://img.shields.io/badge/Level-Beginner-2ea44f)
![Focus](https://img.shields.io/badge/Focus-Python%20Fundamentals-f4b400)

A friendly, hands-on Python fundamentals repository for beginners.

> [!TIP]
> Read an example, run it, change one value, and run it again. Small experiments are the fastest way to learn.

This project teaches Python from scratch with practical examples focused on:

- ✍️ Strings
- 🔢 Numbers and input
- ✅ Conditionals
- 🔁 Loops
- 🧩 Functions

## 🚀 Quick Start

### Run locally

```bash
python "Python Learn.py"
```

The interactive menu lets you run one topic at a time or all topics together.

### Run in the browser

Open the built-in playground: **[index.html](index.html)**

It uses Pyodide to run Python directly in your browser (no local installation needed).

## 🧭 Learning Path at a Glance

| Topic | What you'll practice | Menu option |
| --- | --- | --- |
| Hello World & Basics | Variables, printing, data types | `1` |
| Strings | Indexing, slicing, escape chars, f-strings, methods | `2` |
| Numbers & Input | Arithmetic, conversions, `math` functions | `3` |
| Conditionals | `if` / `elif` / `else`, comparison and logical operators | `4` |
| Loops | `for`, `while`, nested loops, `break` | `5` |
| Functions | Parameters, return values, defaults, `*args` | `6` |
| Run all topics | Practice everything in one go | `7` |

## 📚 What You Will Learn

- Python syntax, variables, and basic data types
- Strings, indexing, slicing, and string methods
- Numbers, arithmetic operators, math, and user input
- `if`, `elif`, `else`, comparisons, and logical operators
- `for` loops, `while` loops, nested loops, and `break`
- Python functions, parameters, return values, default arguments, and `*args`
- Beginner exercises including even-number counting, geometry, physics, and factorials

## 🗂️ Project Structure

- `Python Learn.py` - Python fundamentals examples, exercises, calculations, and interactive menu
- `README.md` - This project guide and explanation of the examples
- `index.html` - Browser playground for running beginner Python snippets

## 🔎 Find This Project

Python for beginners, learn Python, Python basics, Python tutorial, Python practice, Python exercises, Python programming, coding for beginners.

## Complete Program Explanation

### Importing `math`

```python
import math
```

The built-in `math` module provides extra mathematical functions. This project uses `math.ceil()` and `math.factorial()`.

### Hello World and Variables

`run_hello_world()` demonstrates output and variables:

```python
x = 1
rating = 4.99
is_published = False
course_name = "Python Programming"
```

Basic Python data types used here are:

- `int`: whole numbers such as `1000`
- `float`: decimal numbers such as `4.99`
- `bool`: `True` or `False`
- `str`: text such as `"Python Programming"`

The `print()` function displays values. Multiplying a string repeats it:

```python
print("*" * 10)
```

### Strings

`run_strings()` demonstrates text, indexing, slicing, escape characters, f-strings, and string methods.

Triple quotes create a multi-line string:

```python
message = """
Hi John,

My name is Yeshas Sujith
"""
```

String length, indexing, and slicing:

```python
len(course)      # Number of characters
course[0]        # First character
course[-1]       # Last character
course[0:3]      # Index 0 through 2
course[:3]       # Beginning through index 2
course[3:]       # Index 3 through the end
course[:]        # The entire string
```

Python starts indexes at zero. Negative indexes count from the end. The ending index in a slice is excluded.

Escape characters allow special characters inside strings:

- `\"` inserts a double quote
- `\'` inserts a single quote
- `\\` inserts a backslash
- `\n` starts a new line

An f-string inserts variables or expressions into text:

```python
first = "Yeshas"
last = "Sujith"
full = f"{first} {last}"
```

The string methods in the program include:

```python
course.upper()       # Uppercase
course.lower()       # Lowercase
course.title()       # Title Case
course.strip()       # Removes surrounding whitespace
course.find("pro")   # Finds text and returns its index
course.replace("p", "j")
```

Membership checks return `True` or `False`:

```python
"pro" in course
"cool" in course
"swift" not in course
```

### Numbers, Math, and Input

`run_math_and_input()` demonstrates number types, arithmetic, built-in math functions, and user input.

The variable `x` is reassigned as an integer, float, and complex number:

```python
x = 1
x = 1.1
x = 1 + 2j
```

Arithmetic operators:

```python
10 + 3    # Addition: 13
10 - 3    # Subtraction: 7
10 * 3    # Multiplication: 30
10 / 3    # Division: 3.333...
10 // 3   # Floor division: 3
10 % 3    # Remainder: 1
10 ** 3   # Exponent: 1000
```

`x += 3` is shorthand for `x = x + 3`.

The program also uses:

```python
round(2.9)       # Rounds a number
abs(-2.9)        # Absolute value
math.ceil(2.9)   # Rounds upward
```

`input()` always returns a string, so the program converts the response before doing arithmetic:

```python
x = input("x : ")
y = int(x) + 1
```

Non-numeric input causes `int()` to raise a `ValueError`.

### Conditions

`run_conditions()` demonstrates decisions with `if`, `elif`, and `else`:

```python
if temperature > 30:
	print("It's warm")
elif temperature > 20:
	print("It's nice")
else:
	print("It's cold")
```

Indentation defines which statements belong to each condition. The comparison operators used are `>`, `<`, `>=`, `<=`, `==`, and `!=`.

A conditional expression can assign one of two values:

```python
message = "Eligible" if age >= 18 else "Not Eligible"
```

Logical operators combine conditions:

- `and` requires every condition to be true
- `or` requires at least one condition to be true
- `not` reverses a Boolean value

The chained comparison `18 <= age < 65` checks both limits in one expression.

### Loops

`run_loops()` demonstrates repetition with `for`, `while`, nested loops, `break`, and loop `else`.

```python
for number in range(3):
	print(number)
```

This prints `0`, `1`, and `2` because the ending value of `range()` is excluded. Other examples are:

```python
range(1, 4)       # 1, 2, 3
range(1, 10, 2)   # 1, 3, 5, 7, 9
range(2, 10, 2)   # 2, 4, 6, 8
```

The third value is the step size. `break` exits a loop early. A loop’s `else` block runs only when the loop finishes without using `break`.

Nested loops print every combination of the outer and inner values:

```python
for x in range(5):
	for y in range(3):
		print(f"({x}, {y})")
```

The program also iterates through each character in `"Python"` and each item in `[1, 2, 3, 4, 5]`.

The `while` example continues while its condition is true:

```python
number = 100
while number > 0:
	print(number)
	number //= 2
```

Updating `number` ensures that the loop eventually ends.

### The Interactive Menu

`show_main_menu()` prints the available topics. `show_sub_menu()` prints the choices for the selected topic. `main()` repeatedly displays the menu, reads input, removes extra spaces with `.strip()`, converts input to lowercase with `.lower()`, and calls the matching function.

The program accepts numbers and words such as `1`, `strings`, `run all`, `quit`, and `exit`.

The entry-point check runs the menu when this file is executed directly:

```python
if __name__ == "__main__":
	main()
```

### Counting Even Numbers

The standalone exercise counts even numbers from 1 through 9:

```python
count = 0
for number in range(1, 10):
	if number % 2 == 0:
		count += 1
```

The remainder operator `%` identifies even numbers because even numbers have a remainder of zero when divided by two. The exercise prints `2`, `4`, `6`, `8`, and the count `4`.

### Functions

The first `greet()` function takes no arguments and performs a task by printing messages. The later version accepts two parameters:

```python
def greet(first_name, last_name):
	print(f"Hi {first_name} {last_name}")
```

In `greet("Yeshas", "Sujith")`, `first_name` and `last_name` are parameters, while the two names are arguments.

A function can calculate and return a value:

```python
def increment(number, by):
	return number + by
```

`return` sends a value back to the caller. A function without `return` returns `None`, which represents the absence of a value.

### Keyword and Default Arguments

The increment function can use a keyword argument:

```python
increment(2, by=1)
```

It can also provide a default value:

```python
def increment(number, by=1):
	return number + by

increment(2)  # Uses by=1
```

### Variable-Length Arguments

`*numbers` lets a function receive any number of positional arguments:

```python
def multiply(*numbers):
	total = 1
	for number in numbers:
		total *= number
	return total
```

Calling `multiply(2, 3, 4, 5)` returns `120`. Inside the function, `numbers` is a tuple containing all supplied values.

### Geometry and Physics Calculations

The program calculates the area of a circle:

```python
area_of_circle = 3.14 * radius ** 2
```

This follows $A = \pi r^2$.

It calculates the area of a rectangle:

```python
area_of_rectangle = length * width
```

This follows $A = l \times w$.

It calculates weight using mass and gravity:

```python
weight = mass * gravity
```

This follows $W = mg$ and prints the result in newtons (`N`).

### Factorial Exercise

The final example asks for a whole number and calculates its factorial:

```python
fa = int(input(""))
result = math.factorial(fa)
print(result)
```

A factorial multiplies every positive integer up to a number. For example, `5! = 5 × 4 × 3 × 2 × 1 = 120`.

## Important Learning Notes

- A later function definition replaces an earlier definition with the same name.
- The standalone examples after `main()` run after the menu finishes when the file is executed directly.
- The first variable-length `multiply()` example should use the `numbers` tuple when calculating; the final version demonstrates the correct loop-based approach.
- `input()` returns text, so numeric input must be converted with `int()` or `float()` before arithmetic.

## 🌱 Keep Exploring

This project is intended for learning and experimentation. Feel free to run the examples, test different inputs, change values, and add your own practice snippets.
