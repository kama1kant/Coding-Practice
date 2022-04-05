class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def get_total_rib(l):
            nonlocal ribbons
            return sum(r//l for r in ribbons)

        lmin, lmax = 1, max(ribbons)
        count_min, count_max = get_total_rib(lmax), get_total_rib(lmin)

        if k > count_max or k < count_min:
            return 0

        count, l = count_min, lmax
        while lmin < lmax:
            l = (lmin+lmax+1)//2
            count = get_total_rib(l)

            if k <= count:
                lmin = l
            else:
                lmax = l-1

        return lmin

sol = Solution()
sol.maxLength([9,7,5], 4)
sol.maxLength([100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 1, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000], 49)
