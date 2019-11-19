class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Return the length of the longest substring of the input s

        This function finds the legnth of the longest substring in s
        without repeating characters

        >>> Solution.lengthOfLongestSubstring(None, 'abcabcabb')
        3

        >>> Solution.lengthOfLongestSubstring(None, 'bbbbb')
        1

        >>> Solution.lengthOfLongestSubstring(None, 'pwwkew')
        3
        """
        longestSub = 0
        for i in range(len(s)):
            uniqueChars = []
            for j in range(i, len(s)):
                if s[j] not in uniqueChars:
                    uniqueChars.append(s[j])
                else:
                    if len(uniqueChars) > longestSub:
                        longestSub = len(uniqueChars)
                    break
            if len(uniqueChars) > longestSub:
                longestSub = len(uniqueChars)
        return longestSub

if __name__ == "__main__":
    import doctest
    doctest.testmod()
