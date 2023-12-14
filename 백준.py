def solution(cap, n, deliveries, pickups):
    result = 0
    while sum(deliveries) != 0 and sum(pickups) != 0:
        A, B = min(cap, sum(deliveries)), cap
        cnt = n
        long = 0
        while A != 0:
            if deliveries[cnt-1] != 0:
                long = max(long, cnt)
            if deliveries[cnt-1] < A:
                A -= deliveries[cnt-1]
                deliveries[cnt-1] = 0
            else:
                deliveries[cnt-1] -= A
                A = 0
            if pickups[cnt-1] < B:
                B -= pickups[cnt-1]
                pickups[cnt-1] = 0
            else:
                pickups[cnt-1] -= B
                B = 0
            cnt -= 1
        result += long*2
    return result

print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))