arr=[]
for i in range(5):
    row=list(map(int, input().split()))
    arr.append(row)
for i in range(5):
    for j in range(5):
        if arr[i][j] == 1:
            print(abs(i-2) + abs(j-2))
            break