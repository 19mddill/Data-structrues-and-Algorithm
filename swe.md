# LeetCode Coding Interview Roadmap

> Goal: become interview-ready by mastering **problem-solving patterns**, not by blindly solving hundreds of problems.

## Progress Legend

- [ ] Not started
- [~] Solved, needs review
- [x] Solved confidently
- [*] Must-master

---

# Phase 0 — Big-O

Before grinding problems, be comfortable with:

- O(1)
- O(log n)
- O(n)
- O(n log n)
- O(n^2)
- O(2^n)
- O(n!)

Know why:

- HashMap lookup → usually O(1)
- Binary search → O(log n)
- Sorting → usually O(n log n)
- BFS / DFS → O(V + E)

---

# Phase 1 — Arrays & Strings

## Beginner

- [ ] [*] [1. Two Sum](https://leetcode.com/problems/two-sum/)
- [ ] [*] [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
- [ ] [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- [ ] [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- [ ] [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- [ ] [344. Reverse String](https://leetcode.com/problems/reverse-string/)
- [ ] [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)
- [ ] [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- [ ] [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)
- [ ] [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

## Medium

- [ ] [*] [15. 3Sum](https://leetcode.com/problems/3sum/)
- [ ] [*] [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
- [ ] [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
- [ ] [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
- [ ] [189. Rotate Array](https://leetcode.com/problems/rotate-array/)
- [ ] [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
- [ ] [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

### Pattern

If you see:

> Find a pair...

Think **HashMap** or **Two Pointers**.

If you see:

> Maximum/minimum subarray...

Think **Kadane's algorithm**, **Sliding Window**, or **Prefix Sum** depending on the problem.

---

# Phase 2 — HashMap / HashSet

- [ ] [*] [1. Two Sum](https://leetcode.com/problems/two-sum/)
- [ ] [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
- [ ] [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- [ ] [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)
- [ ] [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)
- [ ] [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
- [ ] [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
- [ ] [387. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/)

### Core idea

Use a HashMap when you need:

```text
value -> information about that value
```

Typical uses:

- Frequency counting
- Seen elements
- Index lookup
- Grouping
- Prefix-sum frequencies

---

# Phase 3 — Two Pointers

- [ ] [*] [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- [ ] [*] [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
- [ ] [*] [15. 3Sum](https://leetcode.com/problems/3sum/)
- [ ] [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
- [ ] [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- [ ] [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)
- [ ] [977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)
- [ ] [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

### Recognition rule

If an array is **sorted** and the question involves a pair:

```text
left ->          <- right
```

is often your first thought.

---

# Phase 4 — Sliding Window

- [ ] [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- [ ] [*] [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [ ] [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
- [ ] [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/)
- [ ] [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
- [ ] [643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)
- [ ] [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

### Recognition rule

Look for:

> longest / shortest / maximum / minimum **contiguous** subarray or substring

Think:

```text
L -> [       window       ] <- R
```

---

# Phase 5 — Stack

- [ ] [*] [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- [ ] [155. Min Stack](https://leetcode.com/problems/min-stack/)
- [ ] [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)
- [ ] [*] [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
- [ ] [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)
- [ ] [853. Car Fleet](https://leetcode.com/problems/car-fleet/)
- [ ] [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)

### Recognition rule

If the problem involves:

- Matching
- Nested structures
- Previous/next greater
- Undo-like behavior

Think **Stack**.

---

# Phase 6 — Binary Search

- [ ] [*] [704. Binary Search](https://leetcode.com/problems/binary-search/)
- [ ] [*] [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)
- [ ] [278. First Bad Version](https://leetcode.com/problems/first-bad-version/)
- [ ] [*] [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- [ ] [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
- [ ] [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)
- [ ] [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)
- [ ] [981. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)

### Recognition rule

When the search space is sorted or can be treated as a **monotonic condition**, think:

> **Binary Search**

Target complexity:

```text
O(log n)
```

---

# Phase 7 — Linked Lists

- [ ] [*] [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- [ ] [*] [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)
- [ ] [*] [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
- [ ] [203. Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)
- [ ] [*] [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
- [ ] [*] [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
- [ ] [143. Reorder List](https://leetcode.com/problems/reorder-list/)
- [ ] [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
- [ ] [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)

### Two-pointer patterns

**Find middle:**

```cpp
slow = slow->next;
fast = fast->next->next;
```

**Find cycle:**

```text
slow + fast
```

**Nth node from the end:**

```text
Two pointers with a fixed gap
```

---

# Phase 8 — Trees

## Binary Tree

- [ ] [*] [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [ ] [*] [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
- [ ] [100. Same Tree](https://leetcode.com/problems/same-tree/)
- [ ] [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)
- [ ] [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)
- [ ] [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)
- [ ] [*] [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [ ] [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)
- [ ] [*] [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
- [ ] [*] [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
- [ ] [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

## Traversals

```text
Preorder:
Root -> Left -> Right

Inorder:
Left -> Root -> Right

Postorder:
Left -> Right -> Root

Level Order:
BFS
```

---

# Phase 9 — BFS / DFS

## DFS

- [ ] [*] [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
- [ ] [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/)
- [ ] [*] [133. Clone Graph](https://leetcode.com/problems/clone-graph/)
- [ ] [733. Flood Fill](https://leetcode.com/problems/flood-fill/)
- [ ] [*] [207. Course Schedule](https://leetcode.com/problems/course-schedule/)
- [ ] [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)

## BFS

- [ ] [*] [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [ ] [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)
- [ ] [127. Word Ladder](https://leetcode.com/problems/word-ladder/)
- [ ] [752. Open the Lock](https://leetcode.com/problems/open-the-lock/)
- [ ] [1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

### Recognition rule

Think **BFS** when looking for:

> shortest number of steps / minimum moves

For an unweighted graph:

```text
BFS -> shortest path
```

---

# Phase 10 — Heap / Priority Queue

- [ ] [*] [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [ ] [*] [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
- [ ] [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)
- [ ] [*] [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)
- [ ] [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- [ ] [1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)

### Recognition rule

If you see:

```text
Top K
Kth largest
Kth smallest
continuously get min/max
```

think:

> **Heap / Priority Queue**

---

# Phase 11 — Intervals

- [ ] [*] [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)
- [ ] [57. Insert Interval](https://leetcode.com/problems/insert-interval/)
- [ ] [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
- [ ] [252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)
- [ ] [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
- [ ] [452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

### Recognition rule

Usually:

```text
sort by start time
then scan
```

---

# Phase 12 — Greedy

- [ ] [*] [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
- [ ] [*] [55. Jump Game](https://leetcode.com/problems/jump-game/)
- [ ] [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/)
- [ ] [134. Gas Station](https://leetcode.com/problems/gas-station/)
- [ ] [763. Partition Labels](https://leetcode.com/problems/partition-labels/)
- [ ] [455. Assign Cookies](https://leetcode.com/problems/assign-cookies/)
- [ ] [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

Ask:

> Can I make the best local choice while still guaranteeing the global answer?

---

# Phase 13 — Backtracking

- [ ] [*] [78. Subsets](https://leetcode.com/problems/subsets/)
- [ ] [*] [46. Permutations](https://leetcode.com/problems/permutations/)
- [ ] [*] [39. Combination Sum](https://leetcode.com/problems/combination-sum/)
- [ ] [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
- [ ] [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
- [ ] [79. Word Search](https://leetcode.com/problems/word-search/)
- [ ] [51. N-Queens](https://leetcode.com/problems/n-queens/)

### Mental model

```text
choose
  |
explore
  |
undo
  |
try next choice
```

Typical skeleton:

```text
backtrack(state):
    if finished:
        record answer
        return

    for each choice:
        make choice
        backtrack(new state)
        undo choice
```

---

# Phase 14 — Dynamic Programming

Do not begin by memorizing solutions.

Learn:

```text
state
transition
base case
```

## Beginner

- [ ] [*] [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
- [ ] [*] [198. House Robber](https://leetcode.com/problems/house-robber/)
- [ ] [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)
- [ ] [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
- [ ] [*] [322. Coin Change](https://leetcode.com/problems/coin-change/)
- [ ] [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)

## Medium

- [ ] [*] [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
- [ ] [*] [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
- [ ] [139. Word Break](https://leetcode.com/problems/word-break/)
- [ ] [91. Decode Ways](https://leetcode.com/problems/decode-ways/)
- [ ] [62. Unique Paths](https://leetcode.com/problems/unique-paths/)
- [ ] [518. Coin Change II](https://leetcode.com/problems/coin-change-ii/)
- [ ] [213. House Robber II](https://leetcode.com/problems/house-robber-ii/)

---

# Phase 15 — Graphs

- [ ] [*] [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
- [ ] [*] [133. Clone Graph](https://leetcode.com/problems/clone-graph/)
- [ ] [*] [207. Course Schedule](https://leetcode.com/problems/course-schedule/)
- [ ] [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
- [ ] [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)
- [ ] [261. Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)
- [ ] [323. Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)
- [ ] [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/)
- [ ] [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

## Algorithms

### BFS

Best for shortest paths in an **unweighted** graph.

```text
O(V + E)
```

### DFS

Useful for:

- Connectivity
- Components
- Cycle detection
- Exploration

```text
O(V + E)
```

### Dijkstra

Use for shortest paths when edge weights are **non-negative**.

Typical implementation:

```text
Priority Queue
+
Relaxation
```

### Floyd-Warshall

Use when you want shortest paths between **every pair** of vertices.

```text
O(V^3)
```

---

# Phase 16 — Union Find / DSU

- [ ] [323. Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)
- [ ] [261. Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)
- [ ] [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/)
- [ ] [721. Accounts Merge](https://leetcode.com/problems/accounts-merge/)
- [ ] [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/)

Know:

```text
find()
union()
path compression
union by rank/size
```

---

# Phase 17 — Bit Manipulation

- [ ] [*] [136. Single Number](https://leetcode.com/problems/single-number/)
- [ ] [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)
- [ ] [338. Counting Bits](https://leetcode.com/problems/counting-bits/)
- [ ] [268. Missing Number](https://leetcode.com/problems/missing-number/)
- [ ] [190. Reverse Bits](https://leetcode.com/problems/reverse-bits/)
- [ ] [371. Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)

Know:

```text
AND  &
OR   |
XOR  ^
NOT  ~
LEFT SHIFT  <<
RIGHT SHIFT >>
```

Especially:

```text
x ^ x = 0
x ^ 0 = x
```

---

# Phase 18 — SQL

Core topics:

- [ ] SELECT / WHERE
- [ ] GROUP BY
- [ ] HAVING
- [ ] ORDER BY
- [ ] INNER JOIN
- [ ] LEFT JOIN
- [ ] RIGHT JOIN
- [ ] Subqueries
- [ ] CTE
- [ ] CASE
- [ ] Window Functions
- [ ] ROW_NUMBER
- [ ] RANK
- [ ] DENSE_RANK

Practice:

- [ ] [176. Second Highest Salary](https://leetcode.com/problems/second-highest-salary/)
- [ ] [182. Duplicate Emails](https://leetcode.com/problems/duplicate-emails/)
- [ ] [183. Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/)
- [ ] [181. Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/)
- [ ] [184. Department Highest Salary](https://leetcode.com/problems/department-highest-salary/)
- [ ] [178. Rank Scores](https://leetcode.com/problems/rank-scores/)
- [ ] [180. Consecutive Numbers](https://leetcode.com/problems/consecutive-numbers/)

---

# The 30 Problems I Would Master First

## Tier 1 — Absolute essentials

1. [ ] [*] **1. Two Sum**
2. [ ] [*] **217. Contains Duplicate**
3. [ ] [*] **242. Valid Anagram**
4. [ ] [*] **121. Best Time to Buy and Sell Stock**
5. [ ] [*] **125. Valid Palindrome**
6. [ ] [*] **20. Valid Parentheses**
7. [ ] [*] **704. Binary Search**
8. [ ] [*] **206. Reverse Linked List**
9. [ ] [*] **141. Linked List Cycle**
10. [ ] [*] **53. Maximum Subarray**

## Tier 2 — Core interview patterns

11. [ ] [*] **15. 3Sum**
12. [ ] [*] **238. Product of Array Except Self**
13. [ ] [*] **3. Longest Substring Without Repeating Characters**
14. [ ] [*] **11. Container With Most Water**
15. [ ] [*] **56. Merge Intervals**
16. [ ] [*] **347. Top K Frequent Elements**
17. [ ] [*] **215. Kth Largest Element in an Array**
18. [ ] [*] **200. Number of Islands**
19. [ ] [*] **102. Binary Tree Level Order Traversal**
20. [ ] [*] **98. Validate Binary Search Tree**

## Tier 3 — Strong interview preparation

21. [ ] [*] **33. Search in Rotated Sorted Array**
22. [ ] [*] **207. Course Schedule**
23. [ ] [*] **133. Clone Graph**
24. [ ] [*] **236. Lowest Common Ancestor of a Binary Tree**
25. [ ] [*] **78. Subsets**
26. [ ] [*] **46. Permutations**
27. [ ] [*] **39. Combination Sum**
28. [ ] [*] **198. House Robber**
29. [ ] [*] **322. Coin Change**
30. [ ] [*] **300. Longest Increasing Subsequence**

---

# Interview Pattern Cheat Sheet

| If you see... | Think... |
|---|---|
| Pair + sorted array | Two pointers |
| Pair + unsorted array | HashMap |
| Longest/shortest contiguous | Sliding window |
| Frequency | HashMap |
| Matching brackets | Stack |
| Next greater element | Monotonic stack |
| Sorted search | Binary search |
| Middle linked list | Slow + fast |
| Linked-list cycle | Slow + fast |
| Tree traversal | DFS/BFS |
| Minimum steps | BFS |
| Top K | Heap |
| Intervals | Sort + scan |
| All combinations | Backtracking |
| Optimal subproblem | DP |
| Connected components | DFS/BFS/DSU |
| Shortest weighted path | Dijkstra |
| All-pairs shortest path | Floyd-Warshall |

---

# How to Solve Each Problem

Use this exact process.

## 1. Understand

Ask:

```text
What exactly is the input?
What exactly must I return?
What are the constraints?
Is the data sorted?
Can there be duplicates?
```

## 2. Brute force

First think:

> What is the simplest solution I can write?

Then calculate its complexity.

## 3. Find the pattern

Ask:

```text
HashMap?
Two pointers?
Sliding window?
Stack?
Binary search?
DFS/BFS?
Heap?
Greedy?
DP?
```

## 4. Implement

Write clean code without looking at the answer.

## 5. Complexity

Always write:

```text
Time: O(...)
Space: O(...)
```

## 6. Test

Test:

```text
normal case
empty/small input
duplicates
already sorted input
single element
maximum/minimum values
```

---

# Problem Log

Use this to track your actual practice.

| # | Problem | Pattern | Difficulty | Time Taken | Solved Alone? | Review |
|---|---|---|---|---:|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |

---

# Mistake Log

Track mistakes instead of only counting solved problems.

| Problem | Mistake | Pattern I Missed | Correct Idea | Review Date |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |

---

# Weekly Routine

## Day 1

- Review old mistakes — 10 min
- 1 Easy — 20–30 min
- 1 Medium — 30–45 min
- Explain both solutions aloud

## Day 2

- 1 Medium
- Re-solve one previously failed problem

## Day 3

- 1 Easy
- 1 Medium

## Day 4

- Pattern review
- Re-solve an old problem without looking

## Day 5

- 1–2 Medium problems

## Day 6

### Timed interview

```text
45 minutes
1–2 problems
No solution lookup
No AI
```

## Day 7

Review only.

Do not constantly add new problems.

---

# The Real Goal

Do **not** aim for:

> "I solved 300 LeetCode problems."

Aim for:

> "When I see a new problem, I can recognize the underlying pattern and build a solution."

A strong target is roughly:

```text
50–70 carefully selected problems
+
multiple re-solves
+
pattern recognition
+
Big-O fluency
+
timed practice
```

This is much more valuable than blindly completing a huge problem count.

---

# Interview Readiness Checklist

Before an interview, I should be able to solve these without help:

- [ ] Two Sum
- [ ] 3Sum
- [ ] Binary Search
- [ ] Sliding Window problem
- [ ] Valid Parentheses
- [ ] Reverse Linked List
- [ ] Linked List Cycle
- [ ] Tree DFS
- [ ] Tree BFS
- [ ] Number of Islands
- [ ] Heap / Top K
- [ ] Merge Intervals
- [ ] Backtracking
- [ ] Basic DP
- [ ] Graph BFS/DFS
- [ ] Dijkstra
- [ ] SQL JOIN/GROUP BY/HAVING

And I should be able to explain:

```text
Why does this work?
What is the time complexity?
What is the space complexity?
What happens on edge cases?
Why is this better than brute force?
```

---

# Personal Rule

When stuck, **don't immediately look at the solution.**

Instead ask:

1. What is the brute-force solution?
2. What makes it slow?
3. What information am I repeatedly calculating?
4. Can I store that information?
5. Is the array sorted?
6. Can two pointers help?
7. Is there a moving contiguous range?
8. Is this a graph/tree?
9. Is there a smaller subproblem?
10. What pattern does this resemble?

That thinking process is the actual interview skill.
