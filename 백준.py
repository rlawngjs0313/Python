import sys
try:
    while True:
        data = int(sys.stdin.readline())
        i = 0
        while True:
            i += 1
            test = "1"*i
            if int(test) % data == 0:
                sys.stdout.write(str(i) + '\n')
                break
except:
    exit()