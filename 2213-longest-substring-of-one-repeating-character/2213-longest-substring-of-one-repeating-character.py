class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        n = len(s)
        arr = list(s)

        # Node: (pre_char, pre_len, suf_char, suf_len, max_len, length)
        size = 1
        while size < n:
            size *= 2
        tree = [None] * (2 * size)

        def make_leaf(ch):
            return (ch, 1, ch, 1, 1, 1)

        def merge(L, R):
            if L is None:
                return R
            if R is None:
                return L
            lp_c, lp_l, ls_c, ls_l, lm, ll = L
            rp_c, rp_l, rs_c, rs_l, rm, rl = R

            length = ll + rl

            pre_char = lp_c
            if lp_l == ll and lp_c == rp_c:
                pre_len = ll + rp_l
            else:
                pre_len = lp_l

            suf_char = rs_c
            if rs_l == rl and rs_c == ls_c:
                suf_len = rl + ls_l
            else:
                suf_len = rs_l

            boundary = 0
            if ls_c == rp_c:
                boundary = ls_l + rp_l

            max_len = max(lm, rm, boundary)

            return (pre_char, pre_len, suf_char, suf_len, max_len, length)

        # build
        for i in range(n):
            tree[size + i] = make_leaf(arr[i])
        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        def update(pos, ch):
            i = size + pos
            tree[i] = make_leaf(ch)
            i //= 2
            while i >= 1:
                tree[i] = merge(tree[2 * i], tree[2 * i + 1])
                i //= 2

        result = []
        for i in range(len(queryIndices)):
            idx = queryIndices[i]
            ch = queryCharacters[i]
            if arr[idx] != ch:
                arr[idx] = ch
                update(idx, ch)
            result.append(tree[1][4])

        return result