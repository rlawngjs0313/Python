import sys
from collections import defaultdict
input = sys.stdin.readline
print = sys.stdout.write

def tree1(node):
    if node == '.':
        return 0
    print(f"{node}")
    tree1(D1[node][0])
    tree1(D1[node][-1])

def tree2(node):
    if node == '.':
        return 0
    tree2(D1[node][0])
    print(f"{node}")
    tree2(D1[node][-1])

def tree3(node):
    if node == '.':
        return 0
    tree3(D1[node][0])
    tree3(D1[node][-1])
    print(f"{node}")


N = int(input())
D1 = defaultdict(list)

for _ in range(N):
    a, b, c =  map(str, input().split())
    D1[a].append(b)
    D1[a].append(c)

tree1("A")
print('\n')
tree2("A")
print('\n')
tree3("A")