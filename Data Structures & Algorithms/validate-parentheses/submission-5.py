class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        temp = []
        p_dict = {"(":")", "[":"]", "{":"}"}

        for p in s:
            # Opening bracket
            if p in "[({":
                temp.append(p_dict[p])

            # Closing bracket
            elif len(temp) == 0 or p != temp.pop():
                return False

        if len(temp) != 0:
            return False

        return True