class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        for x in s:
            freq[x] = freq.get(x, 0) + 1

        longest = 0

        for key in freq:
            l, r = 0, 0
            unmatched = 0
            while r <= len(s) - 1:
                if s[r] == key:
                    longest = max(longest, r - l + 1)
                    r += 1
                else:
                    if unmatched < k:
                        longest = max(longest, r - l + 1)
                        r += 1
                        unmatched += 1
                    else:
                        l += 1
                        if s[l - 1] != key:
                            unmatched -= 1

        return longest