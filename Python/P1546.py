M = int(input())
grade = list(map(int,input().split()))
accum = 0

for i in grade:
    i = (i/max(grade))*100
    accum += i

print(accum/M)