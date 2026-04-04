

nums1 = [1,2]
nums2 = [3,4]

nums = nums1 + nums2




nums.sort()

n = len(nums)
if n % 2 == 0:
    median = (nums[n//2 - 1] + nums[n//2]) / 2
else:
    median = nums[n//2]




class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        nums = nums1 + nums2
        nums.sort()
        n = len(nums)
        if n % 2 == 0:
            median = (nums[n//2 - 1] + nums[n//2]) / 2
        else:
            median = nums[n//2]
        
        return median


Solution().findMedianSortedArrays(nums1, nums2)


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array for optimization
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            # Partition nums1 at i, nums2 at j
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i
            
            # Get the four boundary values
            maxLeft1 = float('-inf') if i == 0 else nums1[i - 1]
            minRight1 = float('inf') if i == m else nums1[i]
            
            maxLeft2 = float('-inf') if j == 0 else nums2[j - 1]
            minRight2 = float('inf') if j == n else nums2[j]
            
            # Check if we found the correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # If total length is even
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                # If total length is odd
                else:
                    return float(max(maxLeft1, maxLeft2))
            
            # Adjust binary search range
            elif maxLeft1 > minRight2:
                right = i - 1
            else:
                left = i + 1
        
        return 0.0


# Test cases
nums1 = [1, 2]
nums2 = [3, 4]
print(Solution().findMedianSortedArrays(nums1, nums2))  # Output: 2.5

nums1 = [1, 3]
nums2 = [2]
print(Solution().findMedianSortedArrays(nums1, nums2))  # Output: 2.0



class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Store sign and work with absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # 32-bit integer limits
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31      # -2147483648
        
        result = 0
        
        while x != 0:
            # Extract last digit
            digit = x % 10
            x //= 10
            
            # Check for overflow before multiplying by 10
            if result > INT_MAX // 10:
                return 0
            
            # Check if adding digit would cause overflow
            if result == INT_MAX // 10 and digit > INT_MAX % 10:
                return 0
            
            result = result * 10 + digit
        
        # Apply sign
        result *= sign
        
        # Final boundary check
        if result < INT_MIN or result > INT_MAX:
            return 0
        
        return result


# Test cases
sol = Solution()
print(sol.reverse(123))       # Output: 321
print(sol.reverse(-123))      # Output: -321
print(sol.reverse(120))       # Output: 21
print(sol.reverse(0))         # Output: 0
print(sol.reverse(1534236469))  # Output: 0 (overflow)
print(sol.reverse(-2147483648)) # Output: 0 (overflow)


class Solution:
    def isSorted(self, nums):
        #your code goes here
	    return nums == nums.sort()

Solution().isSorted(nums1)


class Solution:
    def largestElement(self, nums):
        if not nums:
            return
        largest = nums[0]
        for i in nums:
            if i > largest:
                largest = i
        return largest
    




Solution().SecondlargestElement([])      


class Solution:
    def SecondlargestElement(self, nums):
        if nums or len(nums) < 2:
            return None
        largest = seclargest = float("-inf")
        for i in nums:
            if i > largest:
                seclargest = largest
                largest = i
            elif i > seclargest and i != largest:
                seclargest = i
        return seclargest

Solution().SecondlargestElement([4,4,5,6,2])


nums = []
if nums:
    print("Runs")
else:
    print("Does NOT run")


nums = [2,4,7,1,3, 6, -1]

def bubblesort(nums):
    item_unsorted = len(nums) - 1
    sorted_val = False

    while not sorted_val:
        sorted_val = True
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                nums[i+1] , nums[i] = nums[i], nums[i+1]
                sorted_val = False
        item_unsorted -= 1
    return nums

arr = [4,2,7,1,3]



def insertionsort(arr):
    for i in range(1, len(arr)):
        temp_val = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp_val:
            print("while")
            print(j, arr[j])
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp_val
    return arr
        

insertionsort(arr)





a1, a2 = "raushan", "shanrau"
def anacheck(a1, a2):
    ana1 = {}
    ana2 = {}
    lena1 = len(a1 )
    if lena1 !=  len(a2):
        return False
    for i in range(lena1):
        ana1[a1[i]] = ana1.get(a1[i], 0) + 1
        ana2[a1[i]] = ana2.get(a1[i], 0) + 1
    if ana1 == ana2:
        return True
    return False


ip = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]




def anagram(ip):
    res = {}
    for i in ip:
        count = [0]*26
        for j in i:
            count[ord(j) - ord("a")] += 1
        if str(count) not in res:
            res[str(count)] = [i]
        else:
            res[str(count)].append(i)
    return res.values()

import numpy as np
ip = np.array([[1,2], [3,4]])
ip.flatten()








