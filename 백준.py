# 2022 카카오 인턴쉽 / 성격 유형 검사하기 / 11:57

def solution(survey, choices):
    D1 = {"A":0,"N":0,"R":0,"T":0,"C":0,"F":0,"J":0,"M":0}
    result = []
    for i, j in zip(survey, choices):
        if j < 4:
            D1[i[0]] += 4-j
        elif j > 4:
            D1[i[1]] += j-4
    
    if D1["R"] >= D1["T"]:
        result.append("R")
    else:
        result.append("T")
    if D1["C"] >= D1["F"]:
        result.append("C")
    else:
        result.append("F")
    if D1["J"] >= D1["M"]:
        result.append("J")
    else:
        result.append("M")
    if D1["A"] >= D1["N"]:
        result.append("A")
    else:
        result.append("N")
    
    return "".join(result)