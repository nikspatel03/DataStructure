
wordList = ["fool","foul","foil","fail","fall","pall","poll","pool","cool","pole","pope","pale","sale","sage","page"]
d = {}

for line in wordList:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

print(d)
