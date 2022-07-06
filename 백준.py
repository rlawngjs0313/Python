N = int(input())
def star(N):
    if N == 3:
        return ["***", "* *", "***"]
    result = []
    stars = star(N//3)
    for i in stars:
        result.append(i*3)
    for i in stars:
        result.append(i+' '*(N//3)+i)
    for i in stars:
        result.append(i*3)
    return result
print('\n'.join(star(N)))