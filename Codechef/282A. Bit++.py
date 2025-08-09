n=int(input())
c=0
for i in range(n):
    bits=input().strip('X')
    if bits=='++':
        c+=1
    elif bits=='--':
        c-=1
print(c)