import collections


class solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    ans = 0
    exist = set()
    l = 0
    for r, c in enumerate(s):
        while c in exist:
            exist.remove(s[l])
            l += 1
        exist.add(c)
        ans = max(ans, r - l + 1)

    return ans

solution = solution()
solution.lengthOfLongestSubstring("pwwkew")
