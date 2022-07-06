def pac(num):
    if num == 0:
        return 1
    if num <= 1:
        return num
    else:
        return num * pac(num-1)
print(pac(int(input())))