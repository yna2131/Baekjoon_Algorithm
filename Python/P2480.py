A,B,C = input().split()
A = int(A)
B = int(B)
C = int(C)

if A == B == C:
    print(10000+A*1000)
elif A == B or A == C:
    print(1000+A*100)
elif B == C:
    print(1000+B*100)
else:
    print(100*max(A,B,C))