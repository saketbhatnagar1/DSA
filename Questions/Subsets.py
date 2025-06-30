# Given two arrays a[] and b[] of size m and n respectively, the task is to determine whether b[] is a subset of a[]. Both arrays are not sorted, and elements are distinct.

# Examples: 

# Input: a[] = [11, 1, 13, 21, 3, 7], b[] = [11, 3, 7, 1] 
# Output: true

# Input: a[]= [1, 2, 3, 4, 5, 6], b = [1, 2, 4] 
# Output: true

# Input: a[] = [10, 5, 2, 23, 19], b = [19, 5, 3] 
# Output: false

class Solution:
    #BruteForce fails for duplicates
    def BruteForceSolve(a:list,b:list)->bool:
        
        for  i in range(len(b)):
            match = False
            for j in range(len(a)):
                if a[j] == b[i]: 
                    match = True
                    break    
        return match

    def TwoPointerSolution(a:list, b:list)->bool:
        
        a = sorted(a)
        b = sorted(b)
        i, j = 0, 0  # i -> a, j -> b

        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                i += 1
            elif a[i] > b[j]:
                return False  # b[j] not found in a
            else:
                i += 1
                j += 1

        return j == len(b)
    def OptimizedSolution(a:list,b:list)->bool:
        freq = {}
        #Create a hasmap
        for i in a:
            freq[i] = freq.get(i,0)+1
        for i in b:
            if freq.get(i,0)==0:
                return False
            else:
                freq[i]-=1
        return True
    def areDisjoint(self, a, b):
        freq = {}
        for i in a:
            freq[i] = freq.get(i,0)+1
        for i in b:
            if i in freq:
                return False
        return True
                