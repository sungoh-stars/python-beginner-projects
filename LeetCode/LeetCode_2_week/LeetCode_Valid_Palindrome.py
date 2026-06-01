class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_t = s.lower()

        total = ""
        for text in lower_t:
            if text.isalnum():
                total += text

        return total == total[::-1]
