# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution(object):
    def removeDuplicates(self, s):
        stack = []
        for i in range(0,len(s)):
            if len(stack)>=1 and (stack[-1] == s[i]):
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)