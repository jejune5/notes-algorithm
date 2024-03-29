//
// Created by junjie on 8/14/23.
//

/**
 *
 * 1. 两数之和
提示
简单
17.5K
相关企业
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。



示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]


提示：

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案
 *
 *
 */

#include "unordered_map"
#include <vector>
#include "iostream"

using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> hash;
        for (int i = 0; i < nums.size(); i++)
        {
            int complement = target - nums[i];
            if (hash.find(complement) != hash.end())
            {
                return {hash[complement], i};
            }
            hash[nums[i]] = i;
        }
        return {};
    }
};

int main()
{
    Solution sol;
    std::vector<std::tuple< std::vector<int>, int, std::vector<int> >> exps = {
        {{-2, 1, -3, 4, -1, 2, 1, -5, 4}, 6, {0, 1}},
        {{4, -1, 2, 1}, 6, {0, 2}},
        {{3, 3}, 6, {0, 1}},
    };
    for (const auto &exp : exps)
    {
        auto param1 = std::get<0>(exp);
        auto param2 = std::get<1>(exp);
        auto res = std::get<2>(exp);
        auto result = sol.twoSum(param1, param2);
        
        std::cout << (result == res) << " || ";
        for (auto r : result) {
            std::cout << r << " ";
        }
        std::cout << "|| ";
        for (auto r : res) {
            std::cout << r << " ";
        }
        std::cout << std::endl;
    }
}
