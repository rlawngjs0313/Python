import sys
input = sys.stdin.readline
print = sys.stdout.write

while True:
    try:
        s,t = map(str,input().split())
        for i in t:
            if len(s) != 0 and i == s[0]:
                s = s[1:]

        if s == "":
            print(f"Yes\n")
        else:
            print(f"No\n")
    except:
        exit()