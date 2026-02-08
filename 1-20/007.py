#第10001个素数
prime=[2]
num=3
while(len(prime)<10001):
    is_prime=1
    for i in prime:
        if num%i==0:
            is_prime=0
            break
    if is_prime:
        prime.append(num)
    num=num+2

print(prime[-1])





