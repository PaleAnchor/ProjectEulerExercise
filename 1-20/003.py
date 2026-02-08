num = 600851475143
# num = 12
factor = 0
while num % 2 == 0:
    num = int(num / 2)
for i in range(3, num, 2):
    while num % i == 0:
        num = int(num / i)
    if num == 1:
        factor = i
        break
print(factor)




