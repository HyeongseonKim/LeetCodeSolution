from collections import defaultdict
#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s):
        i = 0   # position for first substring(after ahead repeated part)
        j = 0   # position for counting and last substring
        n = len(s)  # length of string
        worddic = defaultdict(int)  # dictionary for checking repeated part and saving index(save i)
        # ex  if s is 'abc', then worddic will be { 'a' : 0, 'b' : 1, 'c' : 2}
        longest = 0 # longest substring, not repeated

        while i < n and j < n:
            charPart = s[j] # part for checking repeated word
            if charPart in worddic: # checking repeated word
                i = max(worddic.get(charPart) + 1, i)   # save postion + 1 about the repeated part before new one.
                # ex if s is 'abcaefghajkl' and charPart is second 'a', then worddic return first 'a'  index and compare i and a's indexself.
                # after that, s[i, j] is 'bcaefgh' until meeting another repeated part.
            longest = max(longest, j - i + 1)
            # according to i and j after checking repeated parts, s[i, j] means non repeated part.
            worddic[charPart] = j
            j += 1

        return longest
