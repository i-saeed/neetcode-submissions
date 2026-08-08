class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        presence = set()
        r = 0
        l = 0

        while r <= len(s) - 1:
            if s[r] not in presence:
                presence.add(s[r])
                longest = max(longest, r + 1 - l)
            else:
                removal = []
                while l < r:
                    removal.append(s[l])
                    if s[l] == s[r]:
                        l += 1
                        break
                    l += 1
                presence.difference_update(removal)
                presence.add(s[r])
            r += 1

        return longest
        