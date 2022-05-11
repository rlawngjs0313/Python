from sklearn.metrics import jaccard_score


f = open("test.txt", "r")
lines = list(f.read())

for i in lines:
    print(i, end="")

print(lines[0])