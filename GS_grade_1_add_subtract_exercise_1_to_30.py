"""
To generate equations for addition and subtraction for my kids Grade 1 (Ontario, Canada) math exercise.
Addition/Subtraction exercise has the 1 <= bigger number <= 30, 1 <= small number <= 10.
Output: in "add_subtraction_exercise.txt"
"""
import numpy as np


eq_number = 28 * 10  # Assume to generate 10 pages of exercise with 28 equations in each page
count = 0
while count < eq_number:
    big_number = np.random.randint(1, 30)
    small_number = np.random.randint(1, 10)
    left_is_big_number = np.random.randint(0,1)
    if left_is_big_number:
        print("{} + {} = ".format(big_number, small_number),
              file=open("add_subtraction_exercise.txt", mode='a'))
    else:
        print("{} + {} = ".format(small_number, big_number),
              file=open("add_subtraction_exercise.txt", mode='a'))
    count += 1
    left_subtract = np.random.randint(1, 30)
    right_subtract = np.random.randint(1,10)
    if left_subtract > right_subtract:
        print("{} - {} = ".format(left_subtract, right_subtract),
              file=open("add_subtraction_exercise.txt", mode='a'))
        count += 1
