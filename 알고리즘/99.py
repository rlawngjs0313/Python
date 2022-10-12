gugu = ""
for i in range(2, 10):
    gugu += (f"# {i}단 # ")
print(gugu)
for i in range(1, 10):
    gugu = ""
    for k in range(2, 10):
        if k*i >= 10:
            gugu += str(f"{k}X {i}={k*i} ")
        else:
            gugu += str(f"{k}X {i}= {k*i} ")
    print(gugu)