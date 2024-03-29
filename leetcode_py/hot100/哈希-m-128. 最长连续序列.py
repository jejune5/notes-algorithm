"""

128. 最长连续序列
中等
1.9K
相关企业
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。



示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9


提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109

"""

from typing import *

'''
hash + 时间O(n)
'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        max_len = 0
        for n in nums:
            if n - 1 not in nums:
                n_cur = n
                sub_len = 1
                while n_cur + 1 in nums:
                    n_cur += 1
                    sub_len += 1
                max_len = max(max_len, sub_len)
        return max_len


if __name__ == '__main__':
    from utils.solution import solve_batch

    solve_batch(
        Solution,
        [
            ([100, 4, 200, 1, 3, 2], 4),
        ]
    )
