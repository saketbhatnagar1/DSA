#Input => w = [1,3,2,4] n=4  [1,2,3,4] return ans such that ans is max occurance of a number based on the rule that w[i] = w[i]+p[i] and max no. of w[i] are same

#output=>4 as p=[4,2,3,1] modifies w acc to rule w[i] = w[i]+p[i] therefore for p = [1,3,2,4] we get w = [5,5,5,5]
from itertools import permutations
from collections import Counter

def max_common_sum(w):
    n = len(w)
    max_count = 0
    best_p = []

    for p in permutations(range(1, n+1)):
        new_w = [w[i] + p[i] for i in range(n)]
        freq = Counter(new_w)
        most_common = max(freq.values())
        
        if most_common > max_count:
            max_count = most_common
            best_p = p

    return max_count  # or return best_p if you need the permutation too

# Example
w = [1, 3, 2, 4]
print(max_common_sum(w))  # Output: 4