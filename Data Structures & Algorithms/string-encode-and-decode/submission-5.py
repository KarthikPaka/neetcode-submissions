class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "\\&."
        encoded_str = "\\%.".join(strs)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s == "\\&.":
            return []
        decoded_str = s.split("\\%.")
        return decoded_str
