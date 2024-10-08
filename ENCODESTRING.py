class Solution:
    separator:str = "#&$"
     
    def encode(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return f"{strs[0]}{self.separator}"
        else:
            return self.separator.join(strs)
        
    def decode(self, s: str) -> list[str]:
        strCoded = s
        output = []
        while(strCoded.find(self.separator) >= 0):
            sep_i = strCoded.find(self.separator)
            output.append(strCoded[:sep_i])
            strCoded = strCoded[sep_i + len(self.separator):]
        if (len(strCoded) > 0):
            output.append(strCoded)
        
        return output

            
if __name__ == "__main__":
    # s_param = ["neet","code","love","you", "#&$"]
    s_param = ["a"]
    mySol = Solution()
    print(f"Param: {s_param}")
    
    coded = mySol.encode(s_param)
    print(f"Coded: {coded}")
    
    decoded = mySol.decode(coded)
    print(f"Decoded: {decoded}")
    