max = 10001
N1 = set(range(1, max)) # (1,2,3,4,5,6,...,10000) 집합
N2 = set() # 집합

for i in range(1, max):
    temp = i
    for j in str(i):
        temp += int(j)
    N2.add(temp) # 39, 51, 57, ...

# 셀프 넘버
N1 = N1.difference(N2) # 집합요소인 셀프 넘버들
N1 = list(N1) # 정렬 위해 리스트
N1.sort() # 오름차순으로 / .replace()
N1 = str(N1).replace("[", "").replace("]", "").replace(", ", "\n") # O(n) => O(1)
print(N1)