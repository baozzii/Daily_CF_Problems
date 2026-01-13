for _ in range(int(input())):
    n = int(input())
    s = input()
    p1 = [0] * n
    p2 = [0] * n
    for i in range(1, n):
        j = p2[i - 1]
        while j and s[i] == s[j]:
            j = p1[j - 1]
        if s[i] != s[j]:
            j += 1
        p2[i] = j
        j = p1[i - 1]
        while j and s[i] != s[j]:
            j = p1[j - 1]
        if s[i] == s[j]:
            j += 1
        p1[i] = j
    print(*p2)
