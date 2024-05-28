valid = [set() for i in range(12)]
for i in range(3, 12):
    for j in range(1 << i):
        t = bin(j)[2:].zfill(i)
        flag = False
        for m in range(i):
            for z in range(1, i):
                if m - z < 0 or m + z >= i:
                    break
                if t[m - z] == t[m] == t[m + z]:
                    flag = True
        if flag:
            valid[i].add(j)

class Solution:
    def solve(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            cur = 0
            for j in range(i, len(s)):
                cur *= 2
                cur += int(s[j])
                if cur in valid[j - i + 1]:
                    ans += len(s) - j
                    break
        return ans


TC = 1

def main():
    obj = Solution()
    for _ in range(TC):
        s = input()
        print(obj.solve(s))

main()
