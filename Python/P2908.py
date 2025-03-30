A,B = input().split()
tempFirst = ""
tempSecond = ""

for i in reversed(range(3)):
    tempFirst += A[i]
    tempSecond += B[i]

A = int(tempFirst)
B = int(tempSecond)

if A > B:
    print(A)
else:
    print(B)