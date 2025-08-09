n=int(input())
for i in range(n):
    words=input()
    if len(words)<=10:
        print(words)
    else:
        print(words[0]+str(len(words)-2)+words[-1])