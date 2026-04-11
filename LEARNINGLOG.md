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

2. The standard syntax for slicing in Python is `array[start:stop:step]`:
   - `start`: The index where the slice begins (inclusive). Defaults to `0`.
   - `stop`: The index where the slice ends (exclusive). The element at this index is not included.
   - `step`: The increment between elements. Defaults to `1`.

## April 10, 2026
1. In Java, `Arrays.toString()` iterates through every element of the array exactly once, so the time complexity is **O(n)**.
2. To sort a string alphabetically (ascending) in Python, we can use `sorted()` combined with `"".join()`.
3. In Python, `defaultdict` is a subclass of the built-in `dict` class from the `collections` module. It automatically assigns a default value to keys that do not exist.
