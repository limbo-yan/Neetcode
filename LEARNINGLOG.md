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

## April 13, 2026
1. Three `O(nlogn)` sorting algorithms: Merge Sort, Quick Sort, and Heap Sort.

|   | Time Complexity | How it works | Pros | Cons |
|---|---|---|---|---|
| **Merge Sort** | **O(n log n)** (always) | Divide array into halves → recursively sort each half → merge sorted halves. | Stable; guaranteed **O(n log n)** performance. | Not in-place; uses extra memory. |
| **Quick Sort** | Average: **O(n log n)**, Worst: **O(n²)** | Pick a pivot → partition elements around pivot → recursively sort partitions. | Very fast in practice; in-place in typical implementations. | Worst case exists if pivots are poor (usually mitigated with randomization). |
| **Heap Sort** | **O(n log n)** (always) | Build a heap → repeatedly extract max/min to place elements in sorted order. | In-place; guaranteed **O(n log n)** performance. | Not stable; often slower than quicksort in practice. |

## April 14, 2026
1. Python swaps list elements in one line with simultaneous assignment (`arr[i], arr[j] = arr[j], arr[i]`): Python first evaluates and packs the right-hand values into a temporary tuple, then unpacks to the left-hand targets, so original values are preserved without needing a manual temp variable.

## April 15, 2026
1. A Max-Heap is a data structure with the following properties:
   - It is a **complete binary tree**.
   - The value of the root node is the largest among all descendant nodes, and the same property holds for its left and right subtrees.

2. A complete binary tree is a binary tree in which all levels are completely filled except possibly the lowest one, which is filled from the left.
   - It is similar to a full binary tree, but with two key differences:
     - All leaf elements must lean toward the left.
     - The last leaf element might not have a right sibling, so a complete binary tree does not have to be a full binary tree.

3. Array representation rules for a binary tree (0-indexed):
   - If an element is at index `i`, its left child is at `2i + 1`.
   - Its right child is at `2i + 2`.
   - Its parent is at `floor((i - 1) / 2)`.

## April 17, 2026
1. **Basic Priority Queue in Python (`heapq`)**
   - Python’s standard library provides a min-heap via `heapq`, which is commonly used as a priority queue.
   - Core operations:
     - `heapq.heappush(heap, x)`: push item `x` into the heap.
     - `heapq.heappop(heap)`: pop and return the smallest-priority item.
     - `heap[0]`: inspect the current smallest item without popping.
   - Typical complexities:
     - Push: **O(log n)**
     - Pop: **O(log n)**
     - Peek (`heap[0]`): **O(1)**
   - For a max-priority queue, push negative values (for numeric priorities) or store tuples with transformed priority.

   ```python
   import heapq

   pq = []
   heapq.heappush(pq, (2, "write tests"))
   heapq.heappush(pq, (1, "fix bug"))
   heapq.heappush(pq, (3, "refactor"))

   while pq:
       priority, task = heapq.heappop(pq)
       print(priority, task)
   # 1 fix bug
   # 2 write tests
   # 3 refactor
   ```

2. **Bucket Sort**
   - Bucket sort distributes elements into a fixed number of buckets based on value ranges, sorts each bucket, then concatenates buckets.
   - It works best when input values are uniformly distributed over a known range.
   - High-level steps:
     1. Create `k` empty buckets.
     2. Map each element to a bucket by range/index formula.
     3. Sort each bucket (often with insertion sort or built-in sort).
     4. Concatenate buckets in order.
   - Complexity:
     - Average/best case: about **O(n + k)** when distribution is even.
     - Worst case: **O(n²)** if many elements collapse into one bucket and that bucket uses quadratic sorting.
   - Not ideal when distribution is highly skewed or range mapping is unclear.

## April 19, 2026
1. To convert a string to an integer in Python, use the built-in `int()` function by passing the string as an argument. If the string contains a valid base-10 integer representation, `int()` returns the corresponding integer value.

   ```python
   s = "123"
   n = int(s)
   print(n)  # 123
   ```

2. `map()` in Python applies a function to each item of an iterable and returns a lazy iterator of transformed results.
   - Syntax: `map(function, iterable, ...)`
   - Common pattern: wrap with `list()` to materialize values.
   - It can take multiple iterables; in that case, the function must accept the same number of arguments, and iteration stops at the shortest iterable.

   ```python
   nums = [1, 2, 3, 4]
   squares = list(map(lambda x: x * x, nums))
   # [1, 4, 9, 16]

   a = [1, 2, 3]
   b = [10, 20, 30]
   sums = list(map(lambda x, y: x + y, a, b))
   # [11, 22, 33]
   ```

## May 1, 2026
1. **Cycle Sort** is an in-place, unstable, comparison-based sorting algorithm that minimizes memory writes. It works by identifying cycles of elements and rotating each cycle so every element moves directly to its correct index. Because each element is written at most once to its final position, Cycle Sort is especially useful when write operations are expensive.
