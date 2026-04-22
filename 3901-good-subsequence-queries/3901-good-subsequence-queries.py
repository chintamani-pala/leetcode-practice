class Solution:
    def countGoodSubseq(self, nums, p, queries):
        # ---- helpers ----
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(nums)
        arr = nums[:]   # norqaveliq copy
        seg = [0] * (4 * n)

        # ---- build ----
        def build(node, l, r):
            if l == r:
                seg[node] = arr[l] if arr[l] % p == 0 else 0
                return
            mid = (l + r) // 2
            build(2*node+1, l, mid)
            build(2*node+2, mid+1, r)
            seg[node] = gcd(seg[2*node+1], seg[2*node+2])

        # ---- update ----
        def update(node, l, r, idx, val):
            if l == r:
                seg[node] = val if val % p == 0 else 0
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(2*node+1, l, mid, idx, val)
            else:
                update(2*node+2, mid+1, r, idx, val)
            seg[node] = gcd(seg[2*node+1], seg[2*node+2])

        # ---- query ----
        def query(node, l, r, ql, qr):
            if ql > r or qr < l:
                return 0
            if ql <= l and r <= qr:
                return seg[node]
            mid = (l + r) // 2
            return gcd(
                query(2*node+1, l, mid, ql, qr),
                query(2*node+2, mid+1, r, ql, qr)
            )

        # ---- init ----
        count_divisible = sum(1 for x in arr if x % p == 0)

        if n > 0:
            build(0, 0, n - 1)

        ans = 0

        # ---- process queries ----
        for idx, val in queries:
            prev = arr[idx]

            if prev % p == 0:
                count_divisible -= 1
            if val % p == 0:
                count_divisible += 1

            arr[idx] = val
            update(0, 0, n - 1, idx, val)

            total_gcd = query(0, 0, n - 1, 0, n - 1)

            if total_gcd == p:
                if count_divisible < n:
                    ans += 1
                else:
                    if n > 6:
                        ans += 1
                    else:
                        ok = False
                        for i in range(n):
                            left = query(0, 0, n - 1, 0, i - 1)
                            right = query(0, 0, n - 1, i + 1, n - 1)
                            if gcd(left, right) == p:
                                ok = True
                                break
                        if ok:
                            ans += 1

        return ans