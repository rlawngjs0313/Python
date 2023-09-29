def solution(today, terms, privacies):
    D1 = {}
    result = []
    for i in terms:
        D1[i[0]] = int(i[2:])
    
    for idx, i in enumerate(privacies):
        year = int(i[:4])
        mon = int(i[5:7])
        day = int(i[8:10])
        exe = i[11]
        
        year += (mon + D1[exe]) // 12
        mon = (mon + D1[exe]) % 12
        
        date = (year-2000)*12*28 + mon*28 + day
        todayDate = (int(today[:4])-2000)*12*28 + int(today[5:7])*28 + int(today[8:])
        if date <= todayDate:
            result.append(idx+1)
    return result

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))