MOD = 998244353

class Solution:
    def solve(self, n: int, arr: list[int]) -> int:
        s = sum(arr)
        dp = [1] + [0] * s
        ans = 0
        for i in range(n):
            for j in range(s - arr[i], -1, -1):
                dp[j + arr[i]] += dp[j]
                dp[j + arr[i]] %= MOD
        for j in range(s + 1):
            ans += (j + 1) // 2 * dp[j]
            ans %= MOD
        for i in range(n):
            for j in range(arr[i]):
                ans += (arr[i] - (arr[i] + j + 1) // 2) * dp[j]
                ans %= MOD
        return ans

tc = 1

def main():
    obj = Solution()
    for _ in range(tc):
        n = int(input())
        arr = list(map(int, input().split()))
        print(obj.solve(n, arr))

main()
