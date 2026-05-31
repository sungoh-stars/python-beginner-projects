====================================================================
LeetCode Algorithm & Refactoring Log
====================================================================

--------------------------------------------------------------------
📌 LeetCode 217. Contains Duplicate
--------------------------------------------------------------------

1. Initial Approach (Sorting & Linear Scan)
- Code:
  class Solution:
      def containsDuplicate(self, nums: List[int]) -> bool:
          nums.sort()
          for i in range(len(nums) - 1):
              if nums[i] == nums[i + 1]:
                  return True
          return False

- Performance: Runtime Beats 6.94% / Memory Beats 98.18%
- Analysis: While this approach achieved an outstanding memory profile by using O(1) auxiliary space via in-place sorting, it suffered from a significant time bottleneck (O(N log N)) due to the sorting overhead.


2. Refactored Approach (Using Hash Set)
- Code:
  class Solution:
      def containsDuplicate(self, nums: List[int]) -> bool:
          n = set(nums)
          if len(n) < len(nums):
              return True
          return False

- Performance: Runtime Beats 78.45% / Memory Beats 72.01%
- Engineering Conclusion: By sacrificing a small amount of memory space (O(N)), the time complexity was dramatically optimized down to O(N). The hash set approach achieved a massive 1,030.4% speed efficiency improvement, making it a much more optimal solution for large-scale data environments.

💡 Key Takeaway
- set: Mastered utilizing unique collections (hash sets) to verify duplication in linear time by comparing the size of the collection before and after element deduplication.


--------------------------------------------------------------------
📌 LeetCode 242. Valid Anagram
--------------------------------------------------------------------

1. Optimal Approach (Using Frequency Counter)
- Code:
  from collections import Counter

  class Solution:
      def isAnagram(self, s: str, t: str) -> bool:
          return Counter(s) == Counter(t)

- Performance: Runtime Beats 98.41% / Memory Beats 27.48%
- Analysis: Instead of sorting the strings (O(N log N)), this approach counts the frequencies of each character in linear time (O(N)). Comparing two frequency maps directly achieves near-perfect time efficiency.

💡 Key Takeaway
- Counter: Learned how to leverage collections.Counter to generate a character frequency hash map in a single line, bypassing sorting overhead and solving string permutation problems efficiently.
