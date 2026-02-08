num_1=1
num_2=2
sum=2
while num_1+num_2<=4000000:
    a=num_1+num_2
    if a%2==0:
        sum+=a
    num_1=num_2
    num_2=a
print(sum)
