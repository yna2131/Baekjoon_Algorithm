sentence = input()
wordCount = 1

if sentence == " ":
    print(0)
    exit(0)

for i in range(len(sentence)):
    if sentence[i-1] == " " and i-1 != 0 and i > 0:
        wordCount += 1
    elif sentence[i] == " " and i == len(sentence)-1:
        continue

print(wordCount)