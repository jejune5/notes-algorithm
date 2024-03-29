"""

46. 全排列
中等
2.7K
相关企业
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。



示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]


提示：

1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同
"""

from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrace(first=0):
            if first == lens:
                res.append(nums[:])
            for i in range(first, lens):
                nums[first], nums[i] = nums[i], nums[first]
                backtrace(first + 1)
                nums[i], nums[first] = nums[first], nums[i]

        lens = len(nums)
        res = []
        backtrace()
        return res


if __name__ == '__main__':
    from utils.solution import solve_batch

    cases = [
        ([1, 2, 3], sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]))
    ]
    solve_batch(Solution, cases)
