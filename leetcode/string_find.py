function findSubstring(s, words):

    if words is empty:
        return []

    wordLen = length of one word
    wordCount = number of words
    totalLen = wordLen * wordCount

    result = []

    # Step 1: build frequency map of words
    targetMap = hashmap
    for word in words:
        targetMap[word] += 1

    # Step 2: try all offsets
    for offset from 0 to wordLen - 1:

        left = offset
        currentMap = empty hashmap
        count = 0

        # Step 3: move right pointer in steps of wordLen
        for right from offset to len(s) - wordLen step wordLen:

            word = substring(s, right, right + wordLen)

            if word exists in targetMap:

                currentMap[word] += 1
                count += 1

                # If frequency exceeds → shrink window
                while currentMap[word] > targetMap[word]:

                    leftWord = substring(s, left, left + wordLen)
                    currentMap[leftWord] -= 1
                    count -= 1
                    left += wordLen

                # If valid window found
                if count == wordCount:
                    append left to result

            else:
                # Reset window
                clear currentMap
                count = 0
                left = right + wordLen

    return result

nums = [4,5,6,7,0,1,2]
target = 7


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dt = {i:id for id, i in enumerate(nums)}
        str_val = sorted(nums)
        left = 0
        right = len(str_val) - 1
        
        while left < right:
            mid = (left + right) // 2
            if target in str_val[left:mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        if left:
            return dt[str_val[left]]
        else:
            return -1


nums = [999,9, 3,5]
target = 999

Solution().search(nums, target)


class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        dt = {i:id for id, i in enumerate(nums)}
        str_val = sorted(nums)
        while left <= right:
            mid = (left + right) // 2
            
            if str_val[mid] == target:
                return dt[str_val[mid]]
            
            # Left half is sorted
            if str_val[left] <= str_val[mid]:
                if str_val[left] <= target < str_val[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            # Right half is sorted
            else:
                if str_val[mid] < target <= str_val[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1

        
        