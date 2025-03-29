N,M = map(int,input().split())
List = [0 for _ in range(N)]

for i in range(M):
    i,j,k = map(int,input().split())
    for value in range(i-1,j):
        List[value] = k
        
for i in List:
    print(i,end=" ")