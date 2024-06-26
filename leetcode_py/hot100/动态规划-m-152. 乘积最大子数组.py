"""

152. 乘积最大子数组
中等
2.1K
相关企业
给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

测试用例的答案是一个 32-位 整数。

子数组 是数组的连续子序列。



示例 1:

输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。


提示:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
nums 的任何前缀或后缀的乘积都 保证 是一个 32-位 整数


"""

from typing import *


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = pre_max = pre_min = nums[0]
        for n in nums[1:]:
            cur_max = max(pre_max * n, pre_min * n, n)
            cur_min = min(pre_max * n, pre_min * n, n)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res


if __name__ == '__main__':
    from utils.solution import solve_batch

    solve_batch(
        Solution,
        [
            ([2, 3, -2, 4], 6),
        ]
    )
