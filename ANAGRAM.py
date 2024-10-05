class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str_check = t

        for char in s:
            if char in t:
                # print(f"Posicion de {char} es {str_check.find(char)}")
                str_check_fhalf = str_check[:str_check.find(char)]
                str_check_lhalf = str_check[str_check.find(char)+1:]
                str_check = f"{str_check_fhalf}{str_check_lhalf}"
                # print(f"Popeado {char}: {str_check} (len: {len(str_check)})")

        return not len(str_check) > 0
            

if __name__ == "__main__":
    mySolution = Solution()
    s = "anacardo"
    t = "cardoana"

    print(f"Parameter s: {s}, t: {t}")

    print(f"output {mySolution.isAnagram(s,t)}")
    print(t)