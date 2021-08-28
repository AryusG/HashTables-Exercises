rand_dict = {'one': 1, 'two': 2, 'three': 3}

arr = [20, 40, 3, 2, 55, 1, 34, 32, 22, 6]
index = 3
var = [*range(index, len(arr))] + [*range(0, index)]
nums = [3, 3]
tar = 6

class Solution(object):
    def twoSum(self, nums, target):
        result = []
        for num in nums:
            for second_num in nums:
                if nums.index(num) == nums.index(second_num):
                    continue
                elif num + second_num == target:
                    result.append(nums.index(num))
                    result.append(nums.index(second_num))
                    return result

s = Solution()
print(s.twoSum(nums, 6))