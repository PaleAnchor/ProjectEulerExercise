import sys
for i in range(999,900,-1):
    for j in range(i,900,-1):
        s1=str(i*j)
        s2=s1[::-1]
        if(s1==s2):
            print(s1)
            sys.exit()

#sys.exit()直接终止所有循环
            