"""
given a list `lst` and a number `N`, create a new list
that contains each number of the list at most N times w/o reordering.

For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], 
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, 
which leads to [1,2,3,1,2,3]
"""


# Time complexity O(n^2)
def delete_nth_naive(lst, n):
    ans = []
    for num in lst:
        if ans.count(num) < n:
            ans.append(num)
    return ans


# Time Complexity O(n), using hash tables
def delete_nth(lst, n):
    import collections
    result = []
    counts = collections.defaultdict(int) # keep track of occurances

    for i in lst:
        if counts[i] < n:
            result.append(i)
            counts[i] += 1
    return result
