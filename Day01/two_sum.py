
def twoSum(nums, target):
    l = len(nums)
    for i in range(0,l):
        a = nums[i]
        for j in range(i+1,l):
            b = nums[j]
            sum = a+b
            if target==sum:
                return [i,j]

nums = [2,7,11,15]
target =26
res = twoSum(nums,target)
print(res)