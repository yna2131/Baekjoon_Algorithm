N = int(input())
List = map(int, input().split())
accum = 0

V = int(input())

for i in List:
    if i == V:
        accum += 1

print(accum)
    