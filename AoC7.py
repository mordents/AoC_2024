def try_add_multiply(goal,my_list):
    [x*x for x in my_list]
    [x+x for x in my_list]






def get_calculation(input_file):
    all_goals = []
    figs_to_sum = []
    with open(input_file) as f:
        content = f.read()
        nums = content.split()  # This splits the content by spaces
        curr_pos = 0
    for x in range(curr_pos, len(nums)):  # Iterate through the list
        if ':' in nums[x]:  # Check if the value contains a colon
            curr_goal = int(nums[x].replace(":", "")) #Find curr_goal
            all_goals.append(curr_goal)
            curr_pos +=1
        for y in range(curr_pos, len(nums)):
            if ':' in nums[y] and nums[y]!=curr_goal:
                next_goal = int(nums[y].replace(":", ""))
                print(f"This is the current goal {curr_goal} and the next goal {next_goal}")
                # Calculate distance and grab elements between the goals
                distance = y - (curr_pos - 1)
                elements_between = nums[curr_pos:y]
                figs_to_sum.append(elements_between)
                # Update curr_goal and curr_pos for the next iteration
                curr_goal = next_goal
                curr_pos = y + 1
                break
                
if __name__ == "__main__":
    get_calculation('AoC7input.txt')