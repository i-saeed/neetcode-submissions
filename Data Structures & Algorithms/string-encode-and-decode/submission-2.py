class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "None"
        return ":".join(",".join(str(ord(char)) for char in s) for s in strs)

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        decoded = []
        for single_str in s.split(":"):
            chars = []
            for char in single_str.split(","):
                if char:
                    chars.append(chr(int(char)))
            decoded.append("".join(chars))

        return decoded