H,M = input().split()
H = int(H)
M = int(M)

if M < 45:
    if H == 0:
        H = 23
        M += 60
    else:
        H -= 1
        M += 60

print(H, M-45)