D, H, W = map(int, input().split())
print(f"{int(H*(D/(H**2+W**2)**(1/2)))} {int(W*(D/(H**2+W**2)**(1/2)))}")