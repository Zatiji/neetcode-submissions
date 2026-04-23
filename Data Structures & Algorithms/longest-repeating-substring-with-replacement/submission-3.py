class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_lenght = 0
        l = 0
        count = {}

        for r in range(len(s)):
            current_letter = s[r]
            count[current_letter] = 1 + count.get(current_letter, 0)

            while (r - l + 1) - max(count.values()) > k:
                left_letter = s[l]
                count[left_letter] -= 1
                l += 1
            
            max_lenght = max(max_lenght, r - l + 1)
        return max_lenght


