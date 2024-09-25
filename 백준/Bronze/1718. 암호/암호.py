L1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word = input()
encode = input()
encode = encode * (len(word)//len(encode)+1)
for i, j in zip(word,encode):
    if i == ' ':
        print(' ',end='')
        continue
    print(L1[(ord(i)-ord('a'))-(ord(j)-ord('a')+1)],end='')