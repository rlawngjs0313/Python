# 2022 카카오 블라인드 / 신고 결과 받기 / 23:50

from collections import defaultdict

def solution(id_list, report, k):
    banned = defaultdict(int)
    D1 = defaultdict(set)
    S1 = set()
    result = []

    for i in id_list:
        D1[i] = set()
    
    for i in report:
        A, B = map(str, i.split())
        D1[A].add(B)
    
    for i in D1.values():
        for j in i:
            banned[j] += 1
            if banned[j] == k:
                S1.add(j)
    
    for i in D1.values():
        result.append(len(i.intersection(S1)))
    
    return result
    

print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))