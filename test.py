s='1 1 4 10 9 10'
a=s.split(" ")
freq_count = {}
for i in range(len(a)):
    if a[i] in freq_count:
        freq_count[a[i]]+=1
    else:
        freq_count[a[i]]=1
       
print(freq_count)

freq_count={1:5}

