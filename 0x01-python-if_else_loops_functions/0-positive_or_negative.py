#!/usr/bin/python3
import random

number = random.randint(-10, 10)

# Check if the number is positive or negative
if number > 0:
    print(f"The number {number} is positive.")
elif number < 0:
    print(f"The number {number} is negative.")
else:
    print(f"The number {number} is zero.")
