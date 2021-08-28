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

arr = [('Jan 9', 35), ('Jan 10', 30), ('Jan 1', 27), ('Jan 2', 31), ('Jan 3', 23), ('Jan 4', 34),
       ('Jan 5', 37), ('Jan 6', 38), ('Jan 7', 29), ('Jan 8', 30)]
arr_two = [None, None, None]
element = ('Jan 9', 35)

if element in arr_two:
    print(element)