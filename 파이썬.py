f = open("test.txt", "r")
lines = f.read()
f.close()

f2 = open(lines + "\\haha.txt", "r")
print(lines+"\\haha.txt")
for line in f2.readlines():
    print(f2.readlines())