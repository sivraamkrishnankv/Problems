n=int(input())
c=0
for i in range(n):
    surity=list(map(int, input().split()))
    if surity[0] + surity[1] + surity[2] >= 2:
        c+=1
print(c)