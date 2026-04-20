class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            res += f"#{length}:{s}"
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            c = s[i]
            length = ""
            if c == "#":
                i += 1
                while s[i] != ":":
                    length += s[i]
                    i += 1
                size = int(length)
                res.append(s[(i+1):(i+1+size)])
                i = i + size + 1
        return res
                
