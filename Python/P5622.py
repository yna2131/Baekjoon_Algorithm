word = input()
dials = [['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
time = 0

for letter in word:
    for index, dial in enumerate(dials):
        if letter in dial:
            time += 3 + index
            
print(time)
        

