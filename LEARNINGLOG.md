# Learning Log

## April 8, 2026
1. In Python, we can duplicate arrays/lists using multiplication (e.g., `arr * 2`).
2. A very fast one-line duplicate check is:
   ```python
   class Solution:
       def hasDuplicate(self, nums: List[int]) -> bool:
           return len(set(nums)) < len(nums)
   ```
3. Common fixed-length list initialization patterns in Python:
   - `arr = [None] * 10`
   - `arr = [0 for _ in range(10)]`
4. `ord()` in Python returns the Unicode code point of a character, so `ord('a') == 97`, which corresponds to Java's `(int) 'a'`.
