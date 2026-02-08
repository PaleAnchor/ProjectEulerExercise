sum=0
for i in range(1,100):
    for j in range(i+1,101):
        if i!=j:
            sum=sum+i*j 
sum=sum*2
print(sum)
