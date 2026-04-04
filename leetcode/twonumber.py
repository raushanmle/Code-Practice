"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""

# sort the array which is already sorted

def twoSum(numbers, target):
    sum = 0
    left = 0
    right = len(numbers) - 1
    while left < right:
        sum = numbers[left] + numbers[right]
        if sum == target:
            return [left, right]
        elif sum > target:
            right = right - 1
        else:
            left = left + 1

    return []


numbers = [0,0,1,2]
target = 6

twoSum(numbers, target)


def count_word_frequency(sentence):
    # Your code goes here
    res = {}
    lst = sentence.split()
    if len(lst) ==0:
        return {}
    for i in lst:
        if i in res:
            res[i] +=1
        else:
            res[i] = 1
    return res


st = "rausha"
st[::-1]

" ".split(" ")
count_word_frequency("")

def count_word_frequency(sentence):
    # Your code goes here
    res = {}
    for i in sentence.split(" "):
        if i in res:
            res[i] +=1
        else:
            res[i] = 1
    return res

def is_palindromic_tuple(tup):
    # Your code goes here
    strval = "".join(map(str, [1, 2, 3]))
    res = False
    if strval == strval[::-1]:
        return True

tup = [1,2,3,2]


def is_palindromic_tuple(tup):
    # Your code goes here
    strval = "".join(map(str, tup))
    if strval == strval[::-1]:
        return True
    return False



def merge_dicts_with_overlapping_keys(dicts):
    # Your code goes here
    final = {}
    for dt in dicts:
        for i in dt:
            if i in final:
                final[i] = final[i] + dt[i]
            else:
                final[i] = dt[i]
    return final

merge_dicts_with_overlapping_keys([{"a": 1, "b": 2}, {"b": 3, "c": 4}, {"c": 5, "d": 6}])     


[i for i in range(2, 1+2, 2)]


sum([i for i in range(2, 6+2, 2)])

val = 36**.5



def int_to_binary(n):
    """
    Function to convert an integer to its binary representation.
    
    Parameters:
    n (int): The integer to convert.
    
    Returns:
    str: The binary representation of the integer.
    """
    # Your code here
    if n ==0:
        return 0
    bin = ""
    k = abs(n)
    while k > 0:
        qt = k % 2
        bin = str(qt) + bin
        k = k//2
    if n<0:
        return "-" + bin
    
    return bin
        
int_to_binary(-10)

int(-10)

def binary_to_decimal(binary_str):
    """
    Function to convert a binary string to its decimal integer representation.
    
    Parameters:
    binary_str (str): The binary string to convert.
    
    Returns:
    int: The decimal representation of the binary string.
    """
    # Your code here
    res = 0
    binary_str = str(int(binary_str))
    
    for p, i in enumerate(binary_str):
        res +=  (2**int(p)) * int(i)
    if int(binary_str)< 0:
        return -res
    else:
        return res

binary_to_decimal("1011")

1111

not(10)

bin(11)




