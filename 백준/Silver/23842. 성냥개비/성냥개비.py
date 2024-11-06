import sys
from collections import defaultdict
from itertools import product
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
D1 = defaultdict(int)
L1 = [6,2,5,5,4,5,6,3,7,6]

L2 = list(product(range(10),repeat=2))
for i,j in L2:
    D1[(i,j)] = L1[i]+L1[j]

N -= 4
for i in L2:
    ii = str(i).replace('(',"").replace(')',"").replace(',',"").replace(' ',"")
    for j in L2:
        jj = str(j).replace('(',"").replace(')',"").replace(',',"").replace(' ',"")
        for k in L2:
            kk = str(k).replace('(',"").replace(')',"").replace(',',"").replace(' ',"")
            if int(ii)+int(jj)==int(kk) and D1[i]+D1[j]+D1[k]==N:
                print(f"{ii}+{jj}={kk}\n")
                exit()
else:
    print(f"impossible\n")