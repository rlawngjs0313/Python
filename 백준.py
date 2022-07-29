data = input()
for i in data:
    if i.isalpha():
        if 65 <= ord(i) <= 96:
            print(chr(65+((ord(i)+13-65)%26)), end="")
        else:
            print(chr(97+((ord(i)+13-97)%26)), end="")
    else:
        print(i, end="")