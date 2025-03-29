residual = []
accum = 0

for i in range(10):
    number = int(input())
    if number%42 not in residual:
        residual.append(number%42)
        accum += 1
        
print(accum)