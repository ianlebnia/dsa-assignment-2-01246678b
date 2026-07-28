# BCP 210: Data Structures and Algorithms I
# Coursework Assignment 2 — Part A: Algorithmic Complexity Analysis
# Academic Year 2025/2026
#
# Instructions:
#   - Answer questions A1 to A5 directly in the functions and docstrings below.
#   - For written/explanation questions, write your answer in the string returned
#     by the function (or as a clearly labelled print statement).
#   - Do NOT change the function signatures.
# ============================================================================


# --- Provided code for analysis (do not modify) ---

def algorithm_x(records, target):
    for i in range(len(records)):
        for j in range(i, len(records)):
            if records[i] + records[j] == target:
                return (i, j)
    return None


def algorithm_y(records, target):
    seen = {}
    for i, val in enumerate(records):
        complement = target - val
        if complement in seen:
            return (seen[complement], i)
        seen[val] = i
    return None


def algorithm_z(records):
    n = len(records)
    for i in range(1, n):
        key = records[i]
        j = i - 1
        while j >= 0 and records[j] > key:
            records[j + 1] = records[j]
            j -= 1
        records[j + 1] = key
    return records


# ============================================================================
# A1 (4 Marks)
# Determine the worst-case time complexity of algorithm_x.
# Explain which part of the code drives the cost.
# ============================================================================

def a1_analysis():
    """
    Write your analysis here.
    Your answer should state the worst-case time complexity and explain WHY.

    Example format:
        Worst-case time complexity: O(?)
        Space complexity: O(?)
        Explanation: ...
    """
    return """
     Worst-case time complexity: O(N^2)
    Space complexity: O(1)
    Explanation: The outer loop runs N times and the inner loop runs up to N - i times for each i, so the total number of comparisons is about N + (N - 1) + ... + 1 = N(N + 1)/2. This is quadratic time. The extra space used is constant because it only stores a few variables.
    """


# ============================================================================
# A2 (4 Marks)
# Determine the worst-case time complexity of algorithm_y.
# What data structure makes it faster? What is the space trade-off?
# ============================================================================

def a2_analysis():
    """
    Write your analysis here.
    """
    
    return """
     Worst-case time complexity: O(N)
    Space complexity: O(N)
    Data structure that enables the speedup: a hash table (dictionary)
    Space trade-off explanation: The dictionary stores previously seen values and their indices so each lookup and insertion is expected to take O(1) time on average, but it uses extra memory proportional to the number of elements processed.
    """


# ============================================================================
# A3 (4 Marks)
# Identify algorithm_z by name.
# State its best-case and worst-case time complexities and the input that causes each.
# ============================================================================

def a3_analysis():
    """
    Write your analysis here.
    """
    return 
    """
   Algorithm name: Insertion Sort
    Best-case time complexity: O(N)   Input arrangement: the list is already sorted, so each element is inserted with no shifting
    Worst-case time complexity: O(N^2)  Input arrangement: the list is in reverse order, so each new element must move past many earlier elements
    """


# ============================================================================
# A4 (4 Marks)
# Complete the complexity comparison table for N = 1,000,000.
# Return a list of dicts, each with keys: 'complexity', 'operations', 'rank'.
# ============================================================================

def a4_table():
    """
    Fill in the approximate number of operations at N = 1,000,000
    and rank them from 1 (fastest) to 5 (slowest).
    """
  
    return [
         {"complexity": "O(1)",        "operations": "1",  "rank": "1"},
        {"complexity": "O(log N)",    "operations": "≈20",  "rank": "2"},
        {"complexity": "O(N)",        "operations": "1,000,000",  "rank": "3"},
        {"complexity": "O(N log N)",  "operations": "≈20,000,000",  "rank": "4"},
        {"complexity": "O(N^2)",      "operations": "1,000,000,000,000",  "rank": "5"},
    ]


# ============================================================================
# A5 (4 Marks)
# Implement an iterative Fibonacci that runs in O(N) time and O(1) space.
# Then write your explanation of why the naive recursive version is O(2^N).
# ============================================================================

def fibonacci_iterative(n):
    """
    Return the n-th Fibonacci number (0-indexed: fib(0)=0, fib(1)=1).
    Must run in O(N) time and O(1) space.
    Do NOT use recursion.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1

    previous, current = 0, 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current
    return current
    pass


def a5_explanation():
    """
    Explain why the naive recursive Fibonacci is O(2^N) and not O(N).
    """
  
    return """
    Why naive recursion is O(2^N): The recursive definition fib(n) = fib(n - 1) + fib(n - 2) causes the computation to branch into two recursive calls at each level, so the number of calls grows roughly like the Fibonacci sequence and exceeds any linear growth. In the worst case, the call tree contains about 2^N nodes, so the time is exponential.
    How the iterative version achieves O(N) time and O(1) space: It computes the sequence from the bottom up, keeping only the last two Fibonacci values in memory and updating them in a single loop. Because each value is produced once and each loop iteration does constant work, the run time is linear and the extra space is constant.
    """


# ============================================================================
# TEST HARNESS — do not modify
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("Part A: Algorithmic Complexity Analysis")
    print("=" * 60)

    print("\n--- A1 Analysis ---")
    print(a1_analysis())

    print("\n--- A2 Analysis ---")
    print(a2_analysis())

    print("\n--- A3 Analysis ---")
    print(a3_analysis())

    print("\n--- A4 Complexity Table ---")
    for row in a4_table():
        print(f"  {row['complexity']:15s} | ops: {str(row['operations']):20s} | rank: {row['rank']}")

    print("\n--- A5 Fibonacci ---")
    test_cases = [(0, 0), (1, 1), (6, 8), (10, 55)]
    all_pass = True
    for n, expected in test_cases:
        result = fibonacci_iterative(n)
        status = "PASS" if result == expected else f"FAIL (got {result}, expected {expected})"
        print(f"  fibonacci_iterative({n}) = {result}  [{status}]")
        if result != expected:
            all_pass = False
    print(f"\n  All Fibonacci tests passed: {all_pass}")
    print("\n--- A5 Explanation ---")
    print(a5_explanation())
