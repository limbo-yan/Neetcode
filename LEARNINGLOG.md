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

## April 9, 2026
1. `enumerate()` in Python is used to loop over an iterable and get both the index and the element at the same time. It returns an enumerate object that produces pairs in the form `(index, element)`. This removes the need to manually maintain a counter variable during iteration.

   Example:
   ```python
   a = ["Python", "Java", "C++"]
   for i, v in enumerate(a):
       print(i, v)
   ```
   Output:
   ```text
   0 Python
   1 Java
   2 C++
   ```
3. The standard syntax for slicing in Python is `array[start:stop:step]`:
   - `start`: The index where the slice begins (inclusive). Defaults to `0`.
   - `stop`: The index where the slice ends (exclusive). The element at this index is not included.
   - `step`: The increment between elements. Defaults to `1`.

## April 10, 2026
1. In Java, `Arrays.toString()` iterates through every element of the array exactly once, so the time complexity is **O(n)**.
2. To sort a string alphabetically (ascending) in Python, we can use `sorted()` combined with `"".join()`.
   ```python
   "".join(sorted(s))
   ```
4. In Python, `defaultdict` is a subclass of the built-in `dict` class from the `collections` module. It automatically assigns a default value to keys that do not exist.
   ```python
   from collections import defaultdict

   d = defaultdict(int)
   d["a"] += 1   # no KeyError, automatically initializes to 0

   # Common Use Cases
   defaultdict(int)     # 0
   defaultdict(list)    # []
   defaultdict(set)     # set()
   defaultdict(str)     # ""
   ```
   
## April 11, 2026
1. The expression `res |= (1 << i)` sets the **i-th bit** (0-indexed) of `res` to `1` while leaving all other bits unchanged. It is a common bitmask idiom:
   - `1 << i` creates a mask with only the i-th bit set.
   - `|=` applies that mask to set the bit in place.

   In Python:
   ```python
   mask = 1 << i      # create
   x |= mask          # set 1
   x &= ~mask         # set 0
   x ^= mask          # flip
   (x & mask) != 0    # check
   ```

2. The Boyer-Moore Voting Algorithm finds a majority element (an element appearing more than `n / 2` times) in linear time and constant space:
   - It tracks a candidate and counter; matching values increase the counter, differing values decrease it, effectively canceling out non-majority elements.

## April 12, 2026
1. In Java, the `Arrays.fill()` method provides a quick and easy way to fill all or part of an array with a specific value. It is commonly used when you need to populate arrays with default values, which can save you time and code.
   - `Arrays.fill(int[] a, int val)` fills the entire integer array with `val`.

   ```java
   int[] nums = new int[5];
   Arrays.fill(nums, 7);
   // nums = [7, 7, 7, 7, 7]
   ```
   - `Arrays.fill(int[] a, int fromIndex, int toIndex, int val)` fills the range `[fromIndex, toIndex)` with `val`.

   ```java
   int[] nums = {1, 2, 3, 4, 5};
   Arrays.fill(nums, 1, 4, 9);
   // nums = [1, 9, 9, 9, 5]
   ```
