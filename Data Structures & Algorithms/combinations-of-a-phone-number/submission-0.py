class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        number_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(number, curStr):
            if len(curStr) == len(digits):
                result.append(curStr)
                return
            for c in number_map[digits[number]]:
                backtrack(number + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return result