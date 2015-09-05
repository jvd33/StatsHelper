from __future__ import division
import math
from collections import Counter
import sys

"""
Simple program to read in input from a text file and compute Stats problems quickly.
Should be better than minitab!
@author: Joe
"""



'Takes a file and tokenizes the input for calculations.'
def tokenize(f):
    nums = f.read()
    list = nums.split()
    numlist = []
    for i in list:
        numlist.append(float(i)) if '.' in i else numlist.append(int(i))
    return numlist

"""
Sums , or the squares of the numbers.
Flag options: n = regular sum, sq = squares, sd = standard deviation
"""
def sum_nums(nums, flag, mean=0):
    x = 0
    if flag == 'sd':
        for n in nums:
            x += ((n - mean)*(n-mean))
        return x
    if flag == 'sq':
        for n in nums:
            x += n * n
        return x
    for n in nums:
        x += n
    return x

"""
Calculates the standard deviation given a list of numbers.
"""
def calc_std_dev(nums):
    sum = sum_nums(nums, 'sd', calc_mean(nums))
    return math.sqrt(sum/(len(nums)-1))


"""
Calculates the variance.
"""
def calc_var(std, mean):
    return (std/mean)



"""
Calculates the range of the list
"""
def calc_range(nums):
    return max(nums) - min(nums)



"""
Calculates the interquartile range of the sample.
"""
def calc_iqr(nums):
    lst = sorted(nums)
    n = len(nums)
    index1 = (n-1) // 4
    index3 = ((3*n)-1) // 4
    if(n % 2):
        return lst[index1], lst[index3]
    else:
        return (lst[index1]+lst[index1+1])/2.0, (lst[index3] + lst[index3+1])/2.0


"""
Calculates the median of the sample
"""
def calc_median(lst):
    sort = sorted(lst)
    l = len(lst)
    index = (l - 1) // 2

    if (l % 2):
        return sort[index]
    else:
        return (sort[index] + sort[index + 1])/2.0


"""
Calculates the mean of the sample
"""
def calc_mean(nums):
    sum = sum_nums(nums, 0)
    return sum/len(nums)


"""
Main Method
"""
def main():
    try:
        filename = str(sys.argv[1])
    except IndexError:
        print('Usage: python statshelper.py [filename]')
        exit()
    try:
        f = open(filename, 'r')
    except IOError:
        print("File not found.")
        exit()
    nums = tokenize(f)
    mode = Counter(nums)
    q1, q3 = calc_iqr(nums)
    print('\n*************************************************\n')
    print('Standard Deviation: ' + str(calc_std_dev(nums)) + '\n')
    print('Variance Coefficient: ' + str(calc_var(calc_std_dev(nums), calc_mean(nums))) + '\n')
    print('First Quartile: ' + str(q1) + '\n')
    print('Third Quartile: ' + str(q3) + '\n')
    print('Interquartile Range: ' + str((q3 - q1)) + '\n')
    print('Full Range: ' + str(calc_range(nums)) + '\n')
    print('Mean: ' + str(calc_mean(nums)) + '\n')
    print('Median: ' + str(calc_median(nums)) + '\n')
    print('Mode: ' + str(mode.most_common(1)[0][0]) + '\n')
    print('*************************************************\n')
    input('Press any button to exit.')
    exit()

main()