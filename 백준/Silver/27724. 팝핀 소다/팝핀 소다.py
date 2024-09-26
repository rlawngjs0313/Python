import math

# 토너먼트식 경기에서 K 기량으로 이길수있는 경우는 log2_K. 총 토너먼트 경기수는 log2_N.
# 기량이 1,2,3,4... 서로 겹치지 않아 가능함.
N, M, K = map(int, input().split())
Total, K = int(math.log2(N)), int(math.log2(K))
print(min(Total, M+K))