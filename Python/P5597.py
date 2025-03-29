List = [i+1 for i in range(30)]

for i in range(28):
    turnedIn = int(input())
    if turnedIn in List:
        List.remove(turnedIn)
        
for i in List:
    print(i, end=" ")