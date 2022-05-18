N = int(input())
s = list(map(int, input().split()))
s_max = max(s)
for i in range(0,N):
    s[i] = s[i]/s_max*100
print(sum(s)/N)