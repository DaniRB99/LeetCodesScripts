class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        output = []
        for string in strs:
            anagramList = -1
            print(f"Se valida {string}")
            for pos, list_str in enumerate(output):
                checkStr = list_str[0]
                print(f"\tcontra {checkStr}")

                if len(checkStr) == len(string):
                    for char in string:
                        if char in checkStr:
                            strFhalf = checkStr[:checkStr.find(char)]
                            strLhalf = checkStr[checkStr.find(char)+1:]
                            checkStr = f"{strFhalf}{strLhalf}"
                        else:
                            break
                
                    if not len(checkStr)>0:
                        print(f"\tANAGRAMA: {pos}")
                        anagramList = pos
                        break
            
            if anagramList>=0:
                output[anagramList].append(string)
            else: 
                output.append([string])
            print(f"--output {output}")
        return output
    
if __name__ == "__main__":
    str = ["act","pots","tops","cat","stop","hat"]
    print(f"Entrada {str}")
    mySol = Solution()
    print(f"Salida {mySol.groupAnagrams(str)}")