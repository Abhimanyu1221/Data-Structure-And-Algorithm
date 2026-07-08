from typing import List
MOD = 10**9 + 7


class Node:
    def __init__(self, num=0, digit_sum=0, count=0):
        self.num = num          # Concatenated number
        self.digit_sum = digit_sum
        self.count = count      # Number of non-zero digits


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)

        # Precompute powers of 10
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        tree = [Node() for _ in range(4 * n)]

        def merge(left: Node, right: Node) -> Node:
            res = Node()
            res.count = left.count + right.count
            res.digit_sum = left.digit_sum + right.digit_sum
            res.num = (left.num * pow10[right.count] + right.num) % MOD
            return res

        def build(idx, l, r):
            if l == r:
                if s[l] != '0':
                    d = int(s[l])
                    tree[idx] = Node(d, d, 1)
                else:
                    tree[idx] = Node(0, 0, 0)
                return

            mid = (l + r) // 2
            build(idx * 2, l, mid)
            build(idx * 2 + 1, mid + 1, r)
            tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1])

        def query(idx, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[idx]

            if r < ql or l > qr:
                return Node()

            mid = (l + r) // 2

            if qr <= mid:
                return query(idx * 2, l, mid, ql, qr)

            if ql > mid:
                return query(idx * 2 + 1, mid + 1, r, ql, qr)

            left = query(idx * 2, l, mid, ql, qr)
            right = query(idx * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        ans = []

        for l, r in queries:
            node = query(1, 0, n - 1, l, r)
            ans.append((node.num * node.digit_sum) % MOD)

        return ans