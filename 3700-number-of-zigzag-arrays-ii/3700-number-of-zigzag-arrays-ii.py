class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        def mat_mul(A, B):
            sz = len(A)
            C = [[0] * sz for _ in range(sz)]
            for i in range(sz):
                for k in range(sz):
                    if A[i][k]:
                        aik = A[i][k]
                        for j in range(sz):
                            C[i][j] = (C[i][j] + aik * B[k][j]) % MOD
            return C

        def mat_pow(A, p):
            sz = len(A)
            res = [[0] * sz for _ in range(sz)]
            for i in range(sz):
                res[i][i] = 1
            while p:
                if p & 1:
                    res = mat_mul(res, A)
                A = mat_mul(A, A)
                p >>= 1
            return res

        def mat_vec_mul(A, v):
            sz = len(A)
            res = [0] * sz
            for i in range(sz):
                s = 0
                for j in range(sz):
                    s = (s + A[i][j] * v[j]) % MOD
                res[i] = s
            return res

        if n == 1:
            return m

        size = 2 * m
        T = [[0] * size for _ in range(size)]

        for x in range(m):
            for y in range(x):
                T[y + m][x] = 1
            for y in range(x + 1, m):
                T[y][x + m] = 1

        vec = [1] * size
        P = mat_pow(T, n - 1)
        ans = sum(mat_vec_mul(P, vec)) % MOD
        return ans