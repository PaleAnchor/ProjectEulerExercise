fib=[1,1]
def next_fib(fib):
    return fib[-1]+fib[-2]

while len(str(fib[-1]))<1000:
    fib.append(next_fib(fib))

print(len(fib))