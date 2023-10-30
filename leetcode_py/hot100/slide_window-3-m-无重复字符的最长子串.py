"""
3. 无重复字符的最长子串
中等
9.7K
相关企业
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。



示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

"""


# 滑动窗口的方法
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        for i in range(len(s)):
            if s[i] not in occ:
                occ.add(s[i])
                print(occ)
        return 0


from utils.solution import solve_batch

cases = [
    ("abcabcbb", 3,),
    # ("pwwkew", 3,)
]
solve_batch(Solution, cases)
