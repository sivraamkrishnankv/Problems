n,m,a=map(int,input().split())
res= (n//a)+1 if n%a!=0 else n//a
res= res*((m//a)+1) if m%a!=0 else res*(m//a)
print(res)

