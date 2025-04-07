import pandas as pd
import numpy as np

# Retrieve the data (input) provided in Advent of Code part 1
import os

file_path = os.path.join(os.getcwd(), 'data_adventofcode_1.xlsx')
df = pd.ExcelFile(file_path).parse('Sheet1')

# Get the data from the left list
left_list = df['left'].tolist()

# Get the data from the right list
right_list = df['right'].tolist()

# Sort the left list
left_list.sort()

# Sort the right list
right_list.sort()

# Calculate the distances
distance_list = []
for i in range(len(left_list)):
    distance = int(np.abs(left_list[i] - right_list[i]))
    distance_list.append(distance)

# print(f'distance list {distance_list}')

# Sum of distances
distance = sum(distance_list)
print(f'distance is {distance}')  # Displays 2176849 

# Find the common members between left and right
set_left = set(left_list)
set_right = set(right_list)
set_intersection = set_left.intersection(set_right)

# print(set_intersection)

# Calculate the score
score = 0
for member in set_intersection:
    # Find the number of occurrences of each common member in the right list
    counter = right_list.count(member)
    score += counter * member  # Calculate the score
    # print('counter for member:', counter, member)

print(score)  # Displays 23384288