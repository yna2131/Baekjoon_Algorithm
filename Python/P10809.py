S = input()
alphabets = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabets:
    try:
        print(S.index(i),end=" ")
    except ValueError:
        print("-1",end=" ")