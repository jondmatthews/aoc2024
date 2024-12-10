#!/usr/bin/env python3

import fileinput


def find_smallest(num_list):
    least = -1

    for num in num_list:
        if least == -1:
            least = num
            exit
        else:
            if num < least:
                least = num

    return least


left_nums = []
right_nums = []

diffs = 0

for line in fileinput.input():
    temp_nums = line.split()

    left_nums.append(int(temp_nums[0]))
    right_nums.append(int(temp_nums[1]))

i = 0

diffs = 0
for num in left_nums:
    lsmall = find_smallest(left_nums)
    rsmall = find_smallest(right_nums)

    if lsmall < rsmall:
        diff = rsmall - lsmall
    else:
        diff = lsmall - rsmall
    diffs = diffs + diff
    left_nums.remove(lsmall)
    right_nums.remove(rsmall)
print(diffs)

