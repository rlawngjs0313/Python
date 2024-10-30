import sys
input = sys.stdin.readline
print = sys.stdout.write

N, Q = map(int, input().split())
L1 = [0]*(N+2)

vote_max = 0
for _ in range(Q):
    word = list(map(int, input().split()))
    if word[0] == 1:
        L1[word[2]] += word[1]
        if word[2] != N+1:
            vote_max = max(vote_max,L1[word[2]])
    else:
        voting = 0
        A = L1[N+1]+word[1]
        for i in L1[1:N+1]:
            voting += vote_max-i
        B = (A-1-vote_max)*len(L1[1:N+1])+voting
        print(f"{'YES' if A>vote_max and B>=word[2] else 'NO'}\n")