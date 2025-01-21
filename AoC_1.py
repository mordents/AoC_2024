#Locations marked by location ID
#Get lists to match - pair up smallest num in left list with smallest in right list
# Pair up second smallest left with second smallest right
#Then add up distances 
# Get user input and split it into a list

def find_dist(list1,list2):
    dist = 0
    while list1 and list2:
        min1, min2 = min(list1), min(list2)
        curr = abs(min1 - min2)
        dist+=curr
        list1.remove(min1)
        list2.remove(min2)
    return dist

#This time, you'll need to figure out exactly how often each number from the left list appears in the right list. 
# Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.

def similarity_score(list1,list2):
    score = 0 
    for num in list1: 
        count=list2.count(num)
        if count>0:
            score += num * count
    return score

elements = []
left_lst = [] 
right_lst = [] 
with open('input_lists.txt') as f: 
    elements = [int(num) for line in f for num in line.strip().split()] 
    for idx, element in enumerate(elements): 
        if idx % 2 == 0: 
            left_lst.append(element) 
        else: 
            right_lst.append(element) 
        
    
    score = similarity_score(left_lst, right_lst) 
    print(score)
    dist = find_dist(left_lst, right_lst)  
        
        