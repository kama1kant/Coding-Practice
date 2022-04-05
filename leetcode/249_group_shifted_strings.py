class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def get_int_for_char(c):
            return int(ord(c) - ord('a'))

        def get_char_for_int(n):
            return chr(n + ord('a'))

        def get_num_form(s):
            d = 26 - get_int_for_char(s[0])
            new_s = ''
            for i in range(len(s)):
                new_s += get_char_for_int((get_int_for_char(s[i]) + d) % 26)
            return new_s

        nums, ans = [], {}
        for s in strings:
            nums.append([get_num_form(s), s])

        for i in range(len(nums)):
            key = nums[i][0]
            if key not in ans:
                ans[key] = []
            ans[key].append(nums[i][1])

        return list(ans.values())

sol = Solution()
print(sol.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
print(sol.groupStrings(["abc", "am"]))