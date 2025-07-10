# s='1 1 4 10 9 10'
# a=s.split(" ")
# freq_count = {}
# for i in range(len(a)):
#     if a[i] in freq_count:
#         freq_count[a[i]]+=1
#     else:
#         freq_count[a[i]]=1
       
# print(freq_count)

# freq_count={1:5}

# #kickstarter round:

# #there are N houses for sale The ith house costs A dollar 
# #You have Budget of B dollars
# # What is the max numbevr of houses you can buy

# def solve(Houses,Budget):
#     Houses = sorted(Houses)
#     ans = 0
#     sum = 0
#     for i in range(len(Houses)):
       
#         if Houses[i]<Budget:
#             ans+=1
#             sum+=Houses[i]
            
#         else:
#             break
#     return ans



# def HouseForSale():
#     N = int(input("Enter the Number of Houses for Sale"))
#     A = [int(input("Enter the price : ")) for _ in range(N)]
#     B = int(input("Enter your budget"))
#     #max number of houses:
#     ans = solve(Houses=A,Budget=B)
#     return ans

# ans = HouseForSale()
# print(ans)

class Sorting:
    @staticmethod
    def bubbleSort(arr:list)->list:
        n = len(arr)
        for i in range(n-1):
            for j in range(0,n-i-1):  
                swapped = False              #[4,3,1,5,24,2]#[3,4,1,5,24,2]#[3,1,4,5,24,2]#[3,1,4,5,24,2]
                if arr[j]>arr[j+1]:                 
                    arr[j+1],arr[j] = arr[j],arr[j+1]
                    swapped = True
                if swapped:
                    break
        return arr
    @staticmethod
    def insertionSort(arr:list)->list:
        
    
a = Sorting.bubbleSort([4,3,1,5,24,2])