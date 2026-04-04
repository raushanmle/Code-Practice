📌 ARRAYS & STRINGS (30-40 problems)
   - Two pointers: 8
   - Sliding window: 8
   - Prefix sum: 5
   - Matrix: 8
   - String manipulation: 8

📌 LINKED LISTS (15-20 problems)
   - Basic operations: 5
   - Two pointers: 5
   - Reversal & reordering: 5
   - Cycle detection: 3

📌 STACKS & QUEUES (15-20 problems)
   - Stack basics: 5
   - Monotonic stack: 5
   - Queue/Deque: 5
   - Design problems: 3

📌 HASH TABLES (15-20 problems)
   - Frequency counting: 5
   - Two sum variations: 5
   - Grouping/mapping: 5
   - Design (LRU cache): 3

📌 TREES (30-40 problems)
   - Binary tree traversal: 8
   - BST operations: 8
   - Tree construction: 5
   - LCA & paths: 5
   - Trie: 5

📌 GRAPHS (25-30 problems)
   - DFS/BFS: 10
   - Topological sort: 5
   - Union Find: 5
   - Shortest path: 5

📌 DYNAMIC PROGRAMMING (40-50 problems)
   - 1D DP: 12
   - 2D DP: 12
   - Knapsack variants: 8
   - LIS/LCS: 8
   - State machine: 5

📌 BINARY SEARCH (15-20 problems)
   - Basic binary search: 5
   - Search in rotated: 5
   - Search space optimization: 5

📌 BACKTRACKING (15-20 problems)
   - Combinations/permutations: 8
   - Subsets: 5
   - N-Queens variations: 5

📌 GREEDY (10-15 problems)
   - Interval problems: 5
   - Array greedy: 5
   - Two pointer greedy: 3

📌 HEAPS (10-15 problems)
   - Top K elements: 5
   - Merge K lists: 3
   - Median finder: 3

📌 BIT MANIPULATION (8-10 problems)
   - Basic operations: 5
   - Tricks & XOR: 3

---

## 📚 ARRAYS & STRINGS - PROBLEM LIST

A curated list of 40 essential problems organized by pattern.  
These problems cover all major patterns needed for interviews.

**Legend:**
- **Difficulty:** 🟢 Easy | 🟡 Medium | 🔴 Hard
- **Priority:** ⭐ Must Do | ⭐⭐ Important | ⭐⭐⭐ Optional

---

## 🎯 PATTERN 1: TWO POINTERS (8 problems)

**Pattern Overview:**
- Use two pointers moving toward each other or in same direction
- **Time Complexity:** Usually O(n)
- **Space Complexity:** O(1)
- **When to use:** Sorted arrays, palindromes, pair finding

### 1. Two Sum II - Input Array Is Sorted
- **LeetCode:** [#167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
- **Difficulty:** 🟡 Medium
- **Priority:** ⭐ Must Do
- **Pattern:** Two pointers from both ends
- **Hint:** Start from both ends, move based on sum comparison
- **Time:** O(n) | **Space:** O(1)
- **💡 Key Insight:** Sorted array allows binary decision making

### 2. 3Sum
- **LeetCode:** [#15](https://leetcode.com/problems/3sum/)
- **Difficulty:** 🟡 Medium
- **Priority:** ⭐ Must Do
- **Pattern:** Fix one element + two pointers
- **Hint:** Sort first, fix one element, use two pointers for rest
- **Time:** O(n²) | **Space:** O(1)
- **💡 Key Insight:** Avoid duplicates by skipping same values

### 3. Container With Most Water
- **LeetCode:** [#11](https://leetcode.com/problems/container-with-most-water/)
- **Difficulty:** 🟡 Medium
- **Priority:** ⭐ Must Do
- **Pattern:** Two pointers optimizing area
- **Hint:** Move pointer with smaller height
- **Time:** O(n) | **Space:** O(1)
- **💡 Key Insight:** Greedy: always try to increase the limiting factor

### 4. Valid Palindrome
- **LeetCode:** [#125](https://leetcode.com/problems/valid-palindrome/)
- **Difficulty:** 🟢 Easy
- **Priority:** ⭐ Must Do
- **Pattern:** Two pointers from both ends
- **Hint:** Compare characters from both ends, skip non-alphanumeric
- **Time:** O(n) | **Space:** O(1)
- **💡 Key Insight:** Use two pointers to avoid reversing string

### 5. Remove Duplicates from Sorted Array
- **LeetCode:** [#26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- **Difficulty:** 🟢 Easy
- **Priority:** ⭐⭐ Important
- **Pattern:** Slow/fast pointers for in-place modification
- **Hint:** Keep unique elements at the beginning
- **Time:** O(n) | **Space:** O(1)
- **💡 Key Insight:** Slow pointer tracks position for unique elements

### 6. Move Zeroes
- **LeetCode:** [#283](https://leetcode.com/problems/move-zeroes/)
- **Difficulty:** 🟢 Easy
- **Priority:** ⭐⭐ Important
- **Pattern:** Slow/fast pointers for partitioning
- **Hint:** Move non-zero elements to front, fill rest with zeros
- **Time:** O(n) | **Space:** O(1)
- **💡 Key Insight:** Similar to partition in quicksort

### 7. Trapping Rain Water
- **LeetCode:** [#42](https://leetcode.com/problems/trapping-rain-water/)
- **Difficulty:** 🔴 Hard
- **Priority:** ⭐⭐⭐ Optional
- **Pattern:** Two pointers with max tracking
- **Hint:** Track max height from both sides
- **Time:** O(n) | **Space:** O(1)
- **💡 Key Insight:** Water trapped depends on min of left/right max

### 8. Sort Colors
- **LeetCode:** [#75](https://leetcode.com/problems/sort-colors/)
- **Difficulty:** 🟡 Medium
- **Priority:** ⭐⭐ Important
- **Pattern:** Dutch National Flag (3-way partition)
- **Hint:** Use three pointers: low, mid, high
- **Time:** O(n) | **Space:** O(1)
- **💡 Key Insight:** One pass partitioning with 3 pointers

---

## 🎯 PATTERN 2: SLIDING WINDOW (8 problems)

**Pattern Overview:**
- Maintain a window with specific properties, expand/shrink as needed
- **Time Complexity:** Usually O(n)
- **Space Complexity:** O(k) where k is window size or character set
- **When to use:** Subarray/substring problems, consecutive elements

### 9. Best Time to Buy and Sell Stock
- **LeetCode:** [#121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- **Difficulty:** 🟢 Easy
- **Priority:** ⭐ Must Do
- **Pattern:** Single pass with min tracking
- **Hint:** Track minimum price seen so far
- **Time:** O(n) | **Space:** O(1)
- **💡 Key Insight:** Max profit = current - min so far

### 10. Longest Substring Without Repeating Characters
- **LeetCode:** [#3](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- **Difficulty:** 🟡 Medium
- **Priority:** ⭐ Must Do
- **Pattern:** Variable size window with hash map
- **Hint:** Use hash map to track last seen position
- **Time:** O(n) | **Space:** O(min(n, m))
- **💡 Key Insight:** Move left pointer when duplicate found

### 11. Minimum Window Substring
- **LeetCode:** [#76](https://leetcode.com/problems/minimum-window-substring/)
- **Difficulty:** 🔴 Hard
- **Priority:** ⭐ Must Do
- **Pattern:** Variable window with character count
- **Hint:** Expand right, shrink left when valid
- **Time:** O(n + m) | **Space:** O(m)
- **💡 Key Insight:** Use counter to track required vs found characters

### 12. Maximum Subarray (Kadane's Algorithm)
- **LeetCode:** [#53](https://leetcode.com/problems/maximum-subarray/)
- **Difficulty:** 🟡 Medium
- **Priority:** ⭐ Must Do
- **Pattern:** Dynamic window/DP
- **Hint:** Keep adding or start fresh if negative
- **Time:** O(n) | **Space:** O(1)
- **💡 Key Insight:** max_ending_here = max(num, max_ending_here + num)

### 13. Longest Repeating Character Replacement
- **LeetCode:** [#424](https://leetcode.com/problems/longest-repeating-character-replacement/)
- **Difficulty:** 🟡 Medium
- **Priority:** ⭐⭐ Important
- **Pattern:** Variable window with frequency count
- **Hint:** window_length - max_freq <= k
- **Time:** O(n) | **Space:** O(1)
- **💡 Key Insight:** Can replace k chars to make substring valid

### 14. Minimum Size Subarray Sum
- **LeetCode:** [#209](https://leetcode.com/problems/minimum-size-subarray-sum/)
- **Difficulty:** 🟡 Medium
- **Priority:** ⭐⭐ Important
- **Pattern:** Variable window with sum tracking
- **Hint:** Expand until sum >= target, then shrink
- **Time:** O(n) | **Space:** O(1)
- **💡 Key Insight:** Shrink window from left when condition met

### 15. Permutation in String
- **LeetCode:** [#567](https://leetcode.com/problems/permutation-in-string/)
- **Difficulty:** 🟡 Medium
- **Priority:** ⭐⭐⭐ Optional
- **Pattern:** Fixed size window with frequency match
- **Hint:** Use fixed window size = len(s1)
- **Time:** O(n) | **Space:** O(1)
- **💡 Key Insight:** Compare frequency maps of windows

### 16. Sliding Window Maximum
- **LeetCode:** [#239](https://leetcode.com/problems/sliding-window-maximum/)
- **Difficulty:** 🔴 Hard
- **Priority:** ⭐⭐⭐ Optional
- **Pattern:** Fixed window with deque for max tracking
- **Hint:** Use monotonic decreasing deque
- **Time:** O(n) | **Space:** O(k)
- **💡 Key Insight:** Maintain candidates for maximum in order

---

## 🎯 PATTERN 3: PREFIX SUM / CUMULATIVE SUM (5 problems)

**Pattern Overview:**
- Precompute cumulative sums for O(1) range queries
- **Time Complexity:** O(n) preprocessing + O(1) per query
- **When to use:** Range sum queries, subarray sum problems

### 17. Subarray Sum Equals K
- **LeetCode:** [#560](https://leetcode.com/problems/subarray-sum-equals-k/)
- **Difficulty:** 🟡 Medium
- **Priority:** ⭐ Must Do
- **Pattern:** Prefix sum with hash map
- **Hint:** Store prefix sums in hash map, check if (sum - k) exists
- **Time:** O(n) | **Space:** O(n)
- **💡 Key Insight:** If prefix_sum[i] - prefix_sum[j] = k, found subarray

### 18. Continuous Subarray Sum
- **LeetCode:** [#523](https://leetcode.com/problems/continuous-subarray-sum/)
- **Difficulty:** 🟡 Medium
- **Priority:** ⭐⭐ Important
- **Pattern:** Prefix sum modulo with hash map
- **Hint:** Store (sum % k) with indices
- **Time:** O(n) | **Space:** O(min(n, k))
- **💡 Key Insight:** Same remainder means divisible difference

### 19. Product of Array Except Self
- **LeetCode:** [#238](https://leetcode.com/problems/product-of-array-except-self/)
- **Difficulty:** 🟡 Medium
- **Priority:** ⭐ Must Do
- **Pattern:** Prefix & suffix products
- **Hint:** Calculate left products, then right products in one array
- **Time:** O(n) | **Space:** O(1)
- **💡 Key Insight:** Result[i] = leftProduct[i] * rightProduct[i]

### 20. Range Sum Query - Immutable
- **LeetCode:** [#303](https://leetcode.com/problems/range-sum-query-immutable/)
- **Difficulty:** 🟢 Easy
- **Priority:** ⭐⭐ Important
- **Pattern:** Classic prefix sum
- **Hint:** prefix[i] = sum of elements [0...i-1]
- **Time:** O(n) init, O(1) query | **Space:** O(n)
- **💡 Key Insight:** sum(i, j) = prefix[j+1] - prefix[i]

### 21. Find Pivot Index
- **LeetCode:** [#724](https://leetcode.com/problems/find-pivot-index/)
- **Difficulty:** 🟢 Easy
- **Priority:** ⭐⭐⭐ Optional
- **Pattern:** Left sum = right sum check
- **Hint:** leftSum = sum - rightSum - nums[i]
- **Time:** O(n) | **Space:** O(1)
- **💡 Key Insight:** Pivot exists when left_sum == right_sum

---

## 🎯 PATTERN 4: MATRIX / 2D ARRAYS (8 problems)

**Pattern Overview:**
- Navigate 2D arrays with directional traversal or transforms
- **Time Complexity:** Usually O(m*n)
- **Space Complexity:** Varies
- **When to use:** Grid problems, image manipulation, path finding

### 22. Rotate Image
- **LeetCode:** [#48](https://leetcode.com/problems/rotate-image/)
- **Difficulty:** 🟡 Medium
- **Priority:** ⭐ Must Do
- **Pattern:** Matrix transpose + reverse
- **Hint:** Transpose then reverse each row (or reverse then transpose)
- **Time:** O(n²) | **Space:** O(1)
- **💡 Key Insight:** 90° rotation = transpose + row reversal

### 23. Spiral Matrix
- **LeetCode:** [#54](https://leetcode.com/problems/spiral-matrix/)
- **Difficulty:** 🟡 Medium
- **Priority:** ⭐ Must Do
- **Pattern:** Layer-by-layer traversal
- **Hint:** Use 4 boundaries: top, bottom, left, right
- **Time:** O(m*n) | **Space:** O(1)
- **💡 Key Insight:** Process one layer at a time, shrink boundaries

### 24. Set Matrix Zeroes
- **LeetCode:** [#73](https://leetcode.com/problems/set-matrix-zeroes/)
- **Difficulty:** 🟡 Medium
- **Priority:** ⭐ Must Do
- **Pattern:** In-place marking with first row/col
- **Hint:** Use first row and column as markers
- **Time:** O(m*n) | **Space:** O(1)
- **💡 Key Insight:** Store state in matrix itself to save space

### 25. Search a 2D Matrix
- **LeetCode:** [#74](https://leetcode.com/problems/search-a-2d-matrix/)
- **Difficulty:** 🟡 Medium
- **Priority:** ⭐⭐ Important
- **Pattern:** Binary search on 2D array
- **Hint:** Treat as 1D array: mid = row*cols + col
- **Time:** O(log(m*n)) | **Space:** O(1)
- **💡 Key Insight:** Convert 2D coordinates using mid/n and mid%n

### 26. Valid Sudoku
- **LeetCode:** [#36](https://leetcode.com/problems/valid-sudoku/)
- **Difficulty:** 🟡 Medium
- **Priority:** ⭐⭐ Important
- **Pattern:** Hash set validation
- **Hint:** Check rows, cols, and 3x3 boxes separately
- **Time:** O(1) - fixed 9x9 | **Space:** O(1)
- **💡 Key Insight:** Use sets to track seen numbers in each unit

### 27. Game of Life
- **LeetCode:** [#289](https://leetcode.com/problems/game-of-life/)
- **Difficulty:** 🟡 Medium
- **Priority:** ⭐⭐⭐ Optional
- **Pattern:** State encoding for in-place update
- **Hint:** Encode next state in current cell
- **Time:** O(m*n) | **Space:** O(1)
- **💡 Key Insight:** Use extra bits to store next state

### 28. Number of Islands
- **LeetCode:** [#200](https://leetcode.com/problems/number-of-islands/)
- **Difficulty:** 🟡 Medium
- **Priority:** ⭐⭐ Important
- **Pattern:** DFS/BFS on 2D grid
- **Hint:** Mark visited cells, count connected components
- **Time:** O(m*n) | **Space:** O(m*n)
- **💡 Key Insight:** Each DFS explores one island completely

### 29. Word Search
- **LeetCode:** [#79](https://leetcode.com/problems/word-search/)
- **Difficulty:** 🟡 Medium
- **Priority:** ⭐⭐⭐ Optional
- **Pattern:** Backtracking on 2D grid
- **Hint:** Try each direction, backtrack if path fails
- **Time:** O(m*n*4^L) | **Space:** O(L)
- **💡 Key Insight:** Mark visited, explore neighbors, unmark on return

---

## 🎯 PATTERN 5: STRING MANIPULATION (8 problems)

**Pattern Overview:**
- Character manipulation, parsing, pattern matching
- **Time Complexity:** Usually O(n)
- **Space Complexity:** Varies
- **When to use:** Text processing, palindromes, anagrams, encoding

### 30. Valid Anagram
- **LeetCode:** [#242](https://leetcode.com/problems/valid-anagram/)
- **Difficulty:** 🟢 Easy
- **Priority:** ⭐ Must Do
- **Pattern:** Frequency count comparison
- **Hint:** Count characters in both strings and compare
- **Time:** O(n) | **Space:** O(1) - fixed alphabet
- **💡 Key Insight:** Anagrams have identical character counts

### 31. Group Anagrams
- **LeetCode:** [#49](https://leetcode.com/problems/group-anagrams/)
- **Difficulty:** 🟡 Medium
- **Priority:** ⭐ Must Do
- **Pattern:** Hash map with sorted string key
- **Hint:** Use sorted string as key to group anagrams
- **Time:** O(n*k*log(k)) | **Space:** O(n*k)
- **💡 Key Insight:** Sorted anagrams are identical

### 32. Longest Palindromic Substring
- **LeetCode:** [#5](https://leetcode.com/problems/longest-palindromic-substring/)
- **Difficulty:** 🟡 Medium
- **Priority:** ⭐ Must Do
- **Pattern:** Expand around center
- **Hint:** For each center, expand while characters match
- **Time:** O(n²) | **Space:** O(1)
- **💡 Key Insight:** Check both odd and even length palindromes

### 33. Valid Parentheses
- **LeetCode:** [#20](https://leetcode.com/problems/valid-parentheses/)
- **Difficulty:** 🟢 Easy
- **Priority:** ⭐ Must Do
- **Pattern:** Stack for matching
- **Hint:** Push opening brackets, pop and match closing ones
- **Time:** O(n) | **Space:** O(n)
- **💡 Key Insight:** Last opened must be first closed (LIFO)

### 34. Longest Common Prefix
- **LeetCode:** [#14](https://leetcode.com/problems/longest-common-prefix/)
- **Difficulty:** 🟢 Easy
- **Priority:** ⭐⭐ Important
- **Pattern:** Vertical scanning
- **Hint:** Compare character by character across all strings
- **Time:** O(S) - total chars | **Space:** O(1)
- **💡 Key Insight:** Stop at first mismatch

### 35. String to Integer (atoi)
- **LeetCode:** [#8](https://leetcode.com/problems/string-to-integer-atoi/)
- **Difficulty:** 🟡 Medium
- **Priority:** ⭐⭐ Important
- **Pattern:** State machine / careful parsing
- **Hint:** Handle whitespace, sign, overflow, non-digits
- **Time:** O(n) | **Space:** O(1)
- **💡 Key Insight:** Check overflow before multiplying by 10

### 36. Implement strStr()
- **LeetCode:** [#28](https://leetcode.com/problems/implement-strstr/)
- **Difficulty:** 🟢 Easy
- **Priority:** ⭐⭐⭐ Optional
- **Pattern:** Sliding window / KMP algorithm
- **Hint:** Check each position for pattern match
- **Time:** O(n*m) naive, O(n+m) KMP | **Space:** O(1) naive, O(m) KMP
- **💡 Key Insight:** KMP avoids re-comparing matched prefixes

### 37. Decode String
- **LeetCode:** [#394](https://leetcode.com/problems/decode-string/)
- **Difficulty:** 🟡 Medium
- **Priority:** ⭐⭐⭐ Optional
- **Pattern:** Stack for nested structures
- **Hint:** Use stack to handle nested encodings
- **Time:** O(maxK * n) | **Space:** O(n)
- **💡 Key Insight:** Stack stores previous strings and repeat counts

---

## 🎁 ADDITIONAL HIGH-VALUE PROBLEMS

### 38. Merge Intervals
- **LeetCode:** [#56](https://leetcode.com/problems/merge-intervals/)
- **Difficulty:** 🟡 Medium
- **Priority:** ⭐ Must Do
- **Pattern:** Sort + merge overlapping
- **Category:** Intervals

### 39. Insert Interval
- **LeetCode:** [#57](https://leetcode.com/problems/insert-interval/)
- **Difficulty:** 🟡 Medium
- **Priority:** ⭐ Must Do
- **Pattern:** Three-part processing
- **Category:** Intervals

### 40. Missing Number
- **LeetCode:** [#268](https://leetcode.com/problems/missing-number/)
- **Difficulty:** 🟢 Easy
- **Priority:** ⭐⭐ Important
- **Pattern:** Math (sum or XOR)
- **Category:** Bit Manipulation

---

## 📅 40-PROBLEM STUDY PLAN

### **WEEK 1: Two Pointers (8 problems)**
- Start with easy problems (Valid Palindrome, Remove Duplicates)
- Progress to medium (Two Sum II, 3Sum, Container With Most Water)
- Challenge: Trapping Rain Water

### **WEEK 2: Sliding Window (8 problems)**
- Begin with Best Time to Buy Stock
- Master: Longest Substring Without Repeating, Maximum Subarray
- Advanced: Minimum Window Substring, Sliding Window Maximum

### **WEEK 3: Prefix Sum & Matrix (13 problems)**
- Prefix Sum: Subarray Sum Equals K, Product of Array Except Self
- Matrix: Rotate Image, Spiral Matrix, Set Matrix Zeroes
- Grid traversal: Number of Islands

### **WEEK 4: String Manipulation (8 problems)**
- Easy: Valid Anagram, Valid Parentheses, Longest Common Prefix
- Medium: Group Anagrams, Longest Palindromic Substring
- Challenge: Decode String

### **WEEK 5: Review & Bonus (3 problems + revision)**
- Solve bonus interval problems
- Revisit difficult problems from previous weeks
- Practice explaining solutions out loud

---

## 🧠 PROBLEM SOLVING TEMPLATE

### Step-by-step approach to solving any array/string problem:

#### 1. **UNDERSTAND** (5 min)
- What is the input? (array, string, sorted?, duplicates?)
- What is the output? (value, index, boolean, modified array?)
- What are the constraints? (time, space, in-place?)
- What are edge cases? (empty, single element, all same?)

#### 2. **EXAMPLES** (3 min)
- Trace through given examples
- Create your own examples
- Think about edge cases

#### 3. **PATTERN RECOGNITION** (5 min)
- Does it involve subarrays? → Consider sliding window or prefix sum
- Is array sorted? → Consider two pointers or binary search
- Need to track frequency? → Consider hash map
- 2D grid navigation? → Consider DFS/BFS or directional arrays
- String matching/manipulation? → Consider two pointers or stack

#### 4. **BRUTE FORCE** (5 min)
- Write the naive solution first
- Analyze time/space complexity
- This often leads to optimization insights

#### 5. **OPTIMIZE** (10 min)
- Can you eliminate redundant work?
- Can you use extra space to save time? (or vice versa)
- Can you precompute something?
- Does the problem have optimal substructure? (DP hint)

#### 6. **CODE** (15 min)
- Write clean, readable code
- Handle edge cases
- Use meaningful variable names

#### 7. **TEST** (5 min)
- Test with examples from problem
- Test edge cases
- Walk through code line by line

#### 8. **ANALYZE** (2 min)
- State time complexity with explanation
- State space complexity with explanation
- Discuss trade-offs if applicable

---

## ⏱️ QUICK REFERENCE: TIME COMPLEXITIES

### **Common Time Complexities**

| Complexity | Examples |
|------------|----------|
| O(1) | Direct access, hash table lookup |
| O(log n) | Binary search, balanced tree operations |
| O(n) | Single pass through array, two pointers |
| O(n log n) | Sorting, heap operations |
| O(n²) | Nested loops, pairwise comparisons |
| O(n³) | Triple nested loops |
| O(2^n) | Recursive branching (subsets, permutations) |
| O(n!) | All permutations |

### **Pattern → Complexity Mapping**

| Pattern | Time Complexity | Space Complexity |
|---------|----------------|------------------|
| Two Pointers | O(n) | O(1) |
| Sliding Window | O(n) | O(k) |
| Prefix Sum | O(n) | O(n) |
| Hash Map | O(n) | O(n) |
| Sorting | O(n log n) | O(1) or O(n) |
| Binary Search | O(log n) | O(1) |
| DFS/BFS on matrix | O(m*n) | O(m*n) |

---

## 📊 SUMMARY

**TOTAL PROBLEMS: 40**
- ⭐ **Must Do:** 18 problems
- ⭐⭐ **Important:** 17 problems
- ⭐⭐⭐ **Optional:** 5 problems

**Good luck with your preparation!** 🚀
