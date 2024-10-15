D1 = {'q':0,'w':0,'e':0,'r':0,'t':0,'y':0,'u':0,'i':0,'o':0,'p':0,'a':0,'s':0,'d':0,'f':0,'g':0,'h':0,'j':0,'k':0,'l':0,'z':0,'x':0,'c':0,'v':0,'b':0,'n':0,'m':0,' ':0}
L1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

word = input()
D1[' '] = int(input())
result = word[0].upper()

for i, j in zip(L1,list(map(int, input().split()))):
    D1[i] = j

for i, v in enumerate(word):
    if D1[v.lower()] != 0:
        if i+1 < len(word) and word[i+1] == v:
            if word[i-1] == ' ' and v != ' ':
                result += v.upper()
            continue
        D1[v.lower()] -= 1
    else:
        print(-1)
        exit()
    if word[i-1] == ' ' and v != ' ':
        result += v.upper()

for i in result:
    if D1[i.lower()] == 0:
        print(-1)
        break
    else:
        D1[i.lower()] -= 1
else:
    print(result)