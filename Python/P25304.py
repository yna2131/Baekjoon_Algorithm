X = int(input())
N = int(input())
accum = 0

for i in range(N):
    a,b = map(int,input().split())
    accum += a*b
    
if accum == X:
    print("Yes")
else:
    print("No")