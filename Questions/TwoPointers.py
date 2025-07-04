class Solution:
    def __init__(self):
        pass

    def MoveZeroes(self, arr: list) -> list:
        left = 0
        for right in range(len(arr)):
            if arr[right] != 0:
                arr[right], arr[left] = arr[left], arr[right]
                left += 1
        return arr
    