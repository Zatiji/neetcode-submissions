class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        right = 0
        left = 0
        maxLength = 0

        while right < len(s):
            
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            maxLength = max(maxLength, right - left + 1)

            right += 1

        return maxLength