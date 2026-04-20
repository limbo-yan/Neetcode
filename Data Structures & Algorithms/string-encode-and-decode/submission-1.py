class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            res += f"#{length}{s}"
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            c = s[i]
            if c == "#":
                length = int(s[i+1]) - int("0")
                res.append(s[(i+2):(i+2+length)])
                i = i + length + 2
        return res
                
