N,M = map(int,input().split())
baskets = [i+1 for i in range(N)]
temp = []

for i in range(M):
    i,j = map(int,input().split())
    temp = baskets[i-1:j]
    temp.reverse()
    for k in range(j-i+1):
        baskets[k+i-1] = temp[k]
    
        
for i in baskets:
    print(i,end=" ")