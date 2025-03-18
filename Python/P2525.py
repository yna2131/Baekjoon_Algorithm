A,B = input().split()
A = int(A)
B = int(B)
C = int(input())

B = B + C

while B >= 60:
    A += 1
    B -= 60
    if A == 24:
        A = 0

print(A,B)