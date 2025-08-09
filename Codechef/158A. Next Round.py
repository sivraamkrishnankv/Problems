n,k=list(map(int, input().split()))
c=0
scores=list(map(int, input().split()))
for i in range(n):
    if scores[i]>=scores[k-1] and scores[i] > 0:
        c+=1
    else:
        break
print(c)