T = int(input())

for i in range(T):
    R,S = input().split()
    R = int(R)
    result = ""
    for i in S:
        result += i*R
    print(result)