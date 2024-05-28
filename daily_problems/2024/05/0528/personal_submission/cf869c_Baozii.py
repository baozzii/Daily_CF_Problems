MOD = 998244353

inv = [0] * 5001
fac = [0] * 5001
cur = 1
for i in range(5001):
    cur = (cur * max(i, 1)) % MOD
    fac[i] = cur
    inv[i] = pow(cur, MOD - 2, MOD)

def factorial(n: int) -> int:
    return fac[n]

def comb(n: int, r: int) -> int:
    return factorial(n) * inv[r] % MOD * inv[n - r] % MOD

class Solution:
    def solve(self, a: int, b: int, c: int) -> int:
        def helper(x: int, y: int) -> int:
            ans = 0
            for i in range(min(x, y) + 1):
                ans += comb(x, i) * comb(y, i) * factorial(i)
                ans %= MOD
            return ans
        return (helper(a, b) * helper(b, c) * helper(a, c)) % MOD


TC = 1

def main():
    obj = Solution()
    for _ in range(TC):
        a, b, c = map(int, input().split())
        print(obj.solve(a, b, c))

main()
