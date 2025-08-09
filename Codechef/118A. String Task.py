n=input()
n=n.lower()
for i in n:
    if i not in 'aeiouyAEIUOY':
        print("."+i,end="")