lst = [1, 2, 3, 4, 5, 6, 8, 9]

def even_num(x):
    if x%2 == 0:
        return True
    else:
        return False


def gt5(x):
    if x>5:
        return x
    

    



list(map(gt5, lst))


list(filter(gt5, lst))

import pandas as pd
df= pd.DataFrame({"col1":[1,2,3,2,4,5,6,4,9,6]})

dt = {
    "col1": 5,
    "col2": 7,
    "col3": 6,
    "col4": 9,
    "col5": 5,
    "col6": 10,
}

def gt5(x):
    print(x)
    # if x.values >5:
    #     return x

list(map(gt5, dt))

def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    # Your code here
    fl = [n*"*"]
    if n<=0:
        return []
    elif n<=2:
        return n*fl
    elif n> 2:
        return fl + [f"*{' '* (n-2)}*" for i in range(n-2)] + fl


generate_hollow_square(4)


f"*{' '* (4)}*"


def generate_triangle(n):
    """
    Function to return a right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height and base of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    return [(i+1)*"*" for i in range(n)]


def generate_floyds_triangle(n):
    """
    Function to return the first n rows of Floyd's Triangle as a list of strings.
    
    Parameters:
    n (int): The number of rows in the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of Floyd's Triangle.
    """
    # Your code here
    
    for i in range(n):
        generate_floyds_triangle(i)


generate_floyds_triangle(6)


# 2n-1
# n = 5

def tet(n):
\
    tl = 2*n-1
    lst = [f"{int((tl - i)/2)* ' '}{i*"*"}{int((tl - i)/2)*' '}" for i in range(1, tl, 2)]
    return lst + [tl*"*"]

tet(0)

def generate_pyramid(n):
    """
    Function to return a pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid.
    """
    # Your code here
    tl = 2*n-1
    lst = [f"{int((tl - i)/2)* ' '}{i*"*"}{int((tl - i)/2)*' '}" for i in range(1, tl, 2)]
    return lst + [tl*"*"]

def generate_inverted_pyramid(n):
    """
    Function to return an inverted pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the inverted pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the inverted pyramid.
    """
    # Your code here
    tl = 2*n-1
    lst = [f"{int((tl - i)/2)* ' '}{i*'*'}{int((tl - i)/2)*' '}" for i in range(tl,0, -2)]
    return lst

7//4


def calculate_lift_rounds(n, capacity):
    """
    Function to calculate the number of rounds the lift needs to cover.
    
    Parameters:
    n (int): Total number of people.
    capacity (int): Maximum number of people the lift can carry in one round.
    
    Returns:
    int: The number of rounds required to transport all people to the top floor.
    """
    # Your code here
    rem = n%capacity
    round_int = n//capacity

    if rem>0:
        return round_int + 1
    return round_int
        
calculate_lift_rounds(20, 2)

round_int = 20//2

def reverse_list(lst):
    # Your code goes here
    return lst[:-1]
        








Input: 3
Output: ['  *  ', ' *** ', '*****']
 
Input: 5
Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********']


def max_consecutive_difference(lst):
    # Your code goes here
    maxdiff = 0
    lenlst = len(lst)
    if lenlst <2:
        return maxdiff
    for i in range(lenlst-1):
        
        diff = abs(lst[i+1] - lst[i])
        if diff > maxdiff:
            maxdiff = diff
    return maxdiff
        
lst =[]


if len(lst)>2:
    for i in range(2):
        lst = [lst.pop()] + lst 

[[lst.pop()] + lst for i in range(2)]


def merge_lists_to_dictionary(keys, values):
    # Your code goes here
    dt = {}
    for i in range(min(len(keys), len(values))):
        dt[keys[i]] = values[i]
    return dt
    
keys, values = ['key1', 'key2'], [100]

merge_lists_to_dictionary(keys, values)


dict1, dict2, dict3 = ({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})
def merge_three_dictionaries(dict1, dict2, dict3):
    # Your code goes here
    final_dict = {}
    for dt in [dict1, dict2, dict3]:
        for i, j in dt.items():
            final_dict[i] = j

    
