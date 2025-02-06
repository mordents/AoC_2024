from itertools import product
def evaluate_left_to_right(expression):
    tokens = expression.split()
    result = int(tokens[0])
    i = 1
    while i < len(tokens):
        operator = tokens[i]
        next_number = int(tokens[i + 1])
        if operator == '+':
            result += next_number
        elif operator == '*':
            result *= next_number
        i += 2
    return result
def try_add_multiply(my_list):
    valid_vals = []
    for sublist in my_list:
        goal_str = sublist[0]  # The goal (e.g., '10:')
        goal = int(goal_str.replace(":", "")) 
        numbers = sublist[1:]  # The numbers after the goal (e.g., [5, 5])
        # Create a list of operators for each position between numbers
        operators = ['+', '*']
        num_operators = len(numbers) - 1  # Number of operator positions
        operator_combinations = product(operators, repeat=num_operators)
        # Check each operator combination
        for ops in operator_combinations:
            # Build the expression as a string
            expression = str(numbers[0])  # Start with the first number
            for i in range(num_operators):
                expression += ' ' + ops[i] + ' ' + str(numbers[i + 1])  # Add operator and next number

            # Evaluate the expression manually (left-to-right)
            try:
                result = evaluate_left_to_right(expression)  # Evaluate the expression
                if result == goal:
                    valid_vals.append(goal)  # Add the goal to valid_vals if the condition is met
                    break  # Stop checking further combinations for this goal
            except:
                pass  # Ignore invalid expressions (if any)
    valid_vals_sum = sum(valid_vals)
    
    return valid_vals_sum  # Return the list of valid goals

def get_calculation(input_file):
    all_goals = []  # List to store all goals and their associated numbers
    with open(input_file) as f:
        content = f.read()
        nums = content.split()  # Split the content by spaces

    curr_pos = 0

    while curr_pos < len(nums):
        if ':' in nums[curr_pos]:  # Check if the current element is a goal
            curr_goal = int(nums[curr_pos].replace(":", ""))  # Extract the goal
            curr_pos += 1  # Move to the next position after the goal

            # Collect all numbers after the goal until the next goal or end of list
            elements_after_goal = []
            while curr_pos < len(nums) and ':' not in nums[curr_pos]:
                elements_after_goal.append(int(nums[curr_pos]))  # Convert to integer
                curr_pos += 1

            # Append the goal and its associated numbers as a nested list
            all_goals.append([f"{curr_goal}:", *elements_after_goal])
    
    return all_goals
if __name__ == "__main__":
    all_goals = get_calculation('AoC7input.txt')
    ans=try_add_multiply(my_list=all_goals)
    print(ans)

#The concatenation operator (||) combines the digits from its left and right inputs into a single number. For example, 12 || 345 would become 12345. All operators are still evaluated left-to-right.
#Now, apart from the three equations that could be made true using only addition and multiplication, the above example has three more equations that can be made true by inserting operators:
#156: 15 6 can be made true through a single concatenation: 15 || 6 = 156.
#7290: 6 8 6 15 can be made true using 6 * 8 || 6 * 15.
#192: 17 8 14 can be made true using 17 || 8 + 14.
#Adding up all six test values (the three that could be made before using only + and * plus the new three that can now be made by also using ||) produces the new total calibration result of 11387.
#Using your new knowledge of elephant hiding spots, determine which equations could possibly be true. What is their total calibration result?