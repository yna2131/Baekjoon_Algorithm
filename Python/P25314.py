byte = int(input())
name = ""

while byte >= 4:
    name += "long "
    byte -= 4

print(f"{name}int")