class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        temp = []
        p_dict = {"(":")", "[":"]", "{":"}"}

        for p in s:
            # Opening bracket
            if p in p_dict:
                temp.append(p_dict[p])

            # Closing bracket
            else:
                if len(temp) == 0:
                    return False

                if p != temp[-1]:
                    return False
                
                else:
                    temp.pop()

        # More opening brackets
        if len(temp) != 0:
            return False

        return True