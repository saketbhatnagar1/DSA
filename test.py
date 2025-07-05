# s='1 1 4 10 9 10'
# a=s.split(" ")
# freq_count = {}
# for i in range(len(a)):
#     if a[i] in freq_count:
#         freq_count[a[i]]+=1
#     else:
#         freq_count[a[i]]=1
       
# print(freq_count)

freq_count={1:5}
#kickstarter round:

#there are N houses for sale The ith house costs A dollar 
#You have Budget of B dollars
# What is the max numbevr of houses you can buy

def solve(Houses,Budget):
    Houses = sorted(Houses)
    ans = 0
    sum = 0
    for i in range(len(Houses)):
       
        if Houses[i]<Budget:
            ans+=1
            sum+=Houses[i]
            
        else:
            break
    return ans



def HouseForSale():
    N = int(input("Enter the Number of Houses for Sale"))
    A = [int(input("Enter the price : ")) for _ in range(N)]
    B = int(input("Enter your budget"))
    #max number of houses:
    ans = solve(Houses=A,Budget=B)
    return ans

ans = HouseForSale()
print(ans)