
def superEggDrop(K, N):
    def f(x):
        ans = 0
        r = 1
        for i in range(1, K+1):
            r *= x-i+1
            r //= i
            ans += r
            if ans >= N: break
        return ans

    low, high = 1, N
    while low < high:
        mid = (low + high) // 2
        if f(mid) < N:
            low = mid + 1
        else:
            high = mid
    return low
K=3
N=123
print(superEggDrop(K,N))