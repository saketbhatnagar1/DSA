class Solution:
    def __init__():
        pass
    def MoveZeroes(self,arr:list)->list:
	    left = 0
	    for right in range(len(arr)):
	        if arr[right]:
	            arr[right],arr[left] = arr[left],arr[right] 
	            left+=1
	    return arr