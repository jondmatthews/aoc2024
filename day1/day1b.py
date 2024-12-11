#!/usr/bin/env python3

import fileinput

def count_occurances(number,num_list):
    count = 0
    for num in num_list:
        if (num == number):
            count = count + 1

    return count;

left_nums = []
right_nums = []

sim = 0
num_count = 0

for line in fileinput.input():
    temp_nums = line.split()

    left_nums.append(int(temp_nums[0]))
    right_nums.append(int(temp_nums[1]))
    num_count = num_count + 1


for i in range(num_count):
    sim = sim + (left_nums[i] * count_occurances(left_nums[i], right_nums))

print(sim)

