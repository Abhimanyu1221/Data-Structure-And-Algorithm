class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
        L = len(num)
        digits = [int(ch) for ch in num]

        tt = t
        a = 0
        while tt % 2 == 0:
            tt //= 2; a += 1
        b = 0
        while tt % 3 == 0:
            tt //= 3; b += 1
        c = 0
        while tt % 5 == 0:
            tt //= 5; c += 1
        d = 0
        while tt % 7 == 0:
            tt //= 7; d += 1
        if tt != 1:
            return "-1"

        CONTRIB = [
            (0,0,0,0), (0,0,0,0), (1,0,0,0), (0,1,0,0), (2,0,0,0),
            (0,0,1,0), (1,1,0,0), (0,0,0,1), (3,0,0,0), (0,2,0,0)
        ]

        INF = float('inf')
        dp = [[INF]*(b+1) for _ in range(a+1)]
        dp[0][0] = 0
        pairs = [(1,0),(0,1),(2,0),(1,1),(3,0),(0,2)]
        for i in range(a+1):
            for j in range(b+1):
                if i == 0 and j == 0:
                    continue
                best = INF
                for dc2, dc3 in pairs:
                    pi = i-dc2 if i-dc2 > 0 else 0
                    pj = j-dc3 if j-dc3 > 0 else 0
                    v = dp[pi][pj]
                    if v+1 < best:
                        best = v+1
                dp[i][j] = best

        def min_needed(ra, rb, rc, rd):
            return dp[ra][rb] + rc + rd

        pe2 = [0]*(L+1); pe3 = [0]*(L+1); pe5 = [0]*(L+1); pe7 = [0]*(L+1)
        phz = [False]*(L+1)
        for i in range(L):
            e2,e3,e5,e7 = CONTRIB[digits[i]]
            pe2[i+1] = pe2[i]+e2
            pe3[i+1] = pe3[i]+e3
            pe5[i+1] = pe5[i]+e5
            pe7[i+1] = pe7[i]+e7
            phz[i+1] = phz[i] or (digits[i] == 0)

        if not phz[L] and pe2[L] >= a and pe3[L] >= b and pe5[L] >= c and pe7[L] >= d:
            return num

        Z = None
        for i in range(L):
            if digits[i] == 0:
                Z = i
                break
        top_j = Z if Z is not None else L-1

        def construct_suffix(ra, rb, rc, rd, S):
            res = []
            remaining = S
            for _ in range(S):
                for v in range(1, 10):
                    c2,c3,c5,c7 = CONTRIB[v]
                    na = ra-c2 if ra-c2 > 0 else 0
                    nb = rb-c3 if rb-c3 > 0 else 0
                    nc = rc-c5 if rc-c5 > 0 else 0
                    nd = rd-c7 if rd-c7 > 0 else 0
                    need = min_needed(na, nb, nc, nd)
                    if need <= remaining-1:
                        res.append(str(v))
                        ra,rb,rc,rd = na,nb,nc,nd
                        remaining -= 1
                        break
            return ''.join(res)

        for j in range(top_j, -1, -1):
            dj = digits[j]
            if dj == 9:
                continue
            pfx2,pfx3,pfx5,pfx7 = pe2[j],pe3[j],pe5[j],pe7[j]
            suffix_len = L-1-j
            for pivot in range(dj+1, 10):
                c2,c3,c5,c7 = CONTRIB[pivot]
                ra = a-pfx2-c2; ra = ra if ra>0 else 0
                rb = b-pfx3-c3; rb = rb if rb>0 else 0
                rc = c-pfx5-c5; rc = rc if rc>0 else 0
                rd = d-pfx7-c7; rd = rd if rd>0 else 0
                needed = min_needed(ra,rb,rc,rd)
                if needed <= suffix_len:
                    suffix = construct_suffix(ra,rb,rc,rd,suffix_len)
                    return num[:j] + str(pivot) + suffix

        # --- fixed fallback ---
        min_total = min_needed(a, b, c, d)
        T = max(L + 1, min_total)
        return construct_suffix(a, b, c, d, T)