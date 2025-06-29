class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = [0,0]
        flattened = [elem for row in grid for elem in row]
        flattened = sorted(flattened)
        freq_count = {}
        for i in flattened:
            if i in freq_count:
                freq_count[i]+=1
                ans[0]=i
            else:
                freq_count[i]=1
        n = len(grid) * len(grid[0]) 
        for i in range(1,n+1):
            if i not in freq_count:
                ans[1] = i
                
        return ans


            
            

