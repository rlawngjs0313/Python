<<<<<<< HEAD
num = int(input())
cont = 1
minus_num = 0
while True:
    minus_num += cont*6
    if num == 1:
        print(1)
        break
    elif num - minus_num <= 1:
        print(cont+1)
        break
    else:
        cont += 1
=======
N = int(input())
s = list(map(int, input().split()))
s_max = max(s)
for i in range(0,N):
    s[i] = s[i]/s_max*100
print(sum(s)/N)
>>>>>>> 126d26093b6d3cacc9ed5c44554fedc518e3af74
