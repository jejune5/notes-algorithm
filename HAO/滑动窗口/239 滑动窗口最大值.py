def maxSlidingWindow(nums, k):

    return nums

nums = [1,3,-1,-3,5,3,6,7]
k = 3
res = []

for i in range(len(nums)-k+1):
    res.append(max(nums[i:i+k]))
    print(i)

print(res)