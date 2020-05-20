s = input()
n=len(s);
k=1
if(n%2==0):
    k=int(n/2)
else:
    k=int((n+1)/2)
if(s[:int((n/2))] == s[n-1:k-1:-1]):
    print("YES")
else:
    print("NO")
