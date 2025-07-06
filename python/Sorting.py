class Sorting:
    def __init__(self):
        pass
    @staticmethod
    def BubbleSort(arr):
        n = len(arr)    
    # Traverse through all array elements
        for i in range(n):
            swapped = False

        # Last i elements are already in place
            for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
                if (swapped == False):
                    break


    @staticmethod
    def InsertionSort(arr)->list:
        n = len(arr)
        for i in range(1,n):
            current = arr[i]
            previous_index = i-1

            while previous_index>=0 and arr[previous_index]>current:
                arr[previous_index+1]=arr[previous_index]
                previous_index-=1
            arr[previous_index+1]=current

    @staticmethod
    def selectionSort(arr)->list:
        n = len(arr)
        for i in range(n-1):
            smallest_index = i
            for j in range(i+1,n):
                if arr[j]<arr[smallest_index]:
                    smallest_index = j
            arr[smallest_index],arr[i] = arr[i],arr[smallest_index]


    @staticmethod
    def MergeSort(arr)->list:
        pass
    @staticmethod
    def quickSort(arr)->list:
        pass
                    

TEST_ARRAY = [442,-1,321,34,231,234,1,21,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1]

Sorting.InsertionSort(TEST_ARRAY)
print(TEST_ARRAY)

