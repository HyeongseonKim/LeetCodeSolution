from collections import defaultdict
from collections import Counter
import re
#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def __init__(self):
        self.longest = 0
        #self.count = 0

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        worddic = defaultdict(int)
        #wordlist = []
        length = 0
        rep = 0
        spliter = ""
        mergedpq = []

        for i in s:
            worddic[i] += 1

        worddic_counter = Counter(worddic)

        for i,  j in worddic_counter.most_common(1):
            spliter = i
            rep = j
            for z in range(len(s)):
                p = re.findall('[^%s]*%s{1}[^%s]*'%(spliter,spliter,spliter),s[z:])
                mergedpq +=  p

        if rep <= 1:
            return len(s)
        else:
            for splitedPart in set(mergedpq):
                length = self.lengthOfLongestSubstring(splitedPart)
                if length > self.longest :
                    self.longest = length
        return self.longest


print(Solution().lengthOfLongestSubstring('loddktdji'))
print(Solution().lengthOfLongestSubstring('abeecfabc'))
print(Solution().lengthOfLongestSubstring('bbcaa'))
print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("dvdf"))
print(Solution().lengthOfLongestSubstring("jjsangmxbomryahpekexmyzrzjsu"))
print(Solution().lengthOfLongestSubstring("ianikjekfbfrllbau"))
