class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        has_leading_zero = False

        def get_abbr_arr(abbr):
            nonlocal has_leading_zero
            abbr_arr = []

            for i in range(len(abbr)):
                ele = abbr[i]
                if abbr[i] >= '0' and abbr[i] <= '9':
                    if abbr[i] == '0' and ((len(abbr_arr) <= 0) or isinstance(abbr_arr[-1], str)):
                        has_leading_zero = True

                    ele = int(abbr[i])
                    if len(abbr_arr) > 0 and isinstance(abbr_arr[-1], int):
                        ele += abbr_arr[-1] * 10
                        abbr_arr.pop()
                abbr_arr.append(ele)

            return abbr_arr

        abbr_arr = get_abbr_arr(abbr)
        if has_leading_zero:
            return False

        print(abbr_arr)
        i, j = 0, 0
        while i < len(word) and j < len(abbr_arr):
            if isinstance(abbr_arr[j], int):
                i += abbr_arr[j]
            elif word[i] == abbr_arr[j]:
                i += 1
            else:
                return False
            j += 1
        return True if i == len(word) and j == len(abbr_arr) else False


sol = Solution()
print(sol.validWordAbbreviation("internationalization", "i12iz4n"))
print(sol.validWordAbbreviation("hi", "h01"))
