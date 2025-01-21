#Many invalid characters that should be ignored, even if they look like part of a mul instruction. 
# Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

#For example, consider the following section of corrupted memory:

#xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

#Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

#Scan the corrupted memory for uncorrupted mul instructions. 
# What do you get if you add up all of the results of the multiplications?
import re

# Read input from file
with open("./input_3.txt", "r") as file:
    input_text = file.read()

# Part 1
def part1():
    regex = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(regex, input_text)

    total = 0
    for match in matches:
        a, b = get_numbers(match)
        total += a * b

    print(f"Total: {total}")

# Part 2
def part2():
    regex = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(regex, input_text)

    is_enabled = True  # At the start, mul instructions are enabled
    total = 0

    for match in matches:
        if match == "do()":
            is_enabled = True
        elif match == "don't()":
            is_enabled = False
        elif match.startswith("mul") and is_enabled:
            a, b = get_numbers(match)
            total += a * b

    print(f"Total: {total}")

# Helper function to extract numbers from a match
def get_numbers(match):
    numbers = re.findall(r"\d{1,3}", match)
    return int(numbers[0]), int(numbers[1])

# Execute parts
part1()
part2()
