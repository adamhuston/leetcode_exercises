class Solution:
    def reverseWords(self, s: str) -> str:
        splitted = s.split(" ")
        reversed = splitted[::-1]
        target = [" ", ""]
        cleaned = [word for word in reversed if word not in target]
        print(cleaned)
        resolved = " ".join(cleaned)
        return resolved

a = Solution()
print(
    a.reverseWords("  hello    word ")
)
