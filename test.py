rand_dict = {'one': 1, 'two': 2, 'three': 3}

arr = [20, 40, 3, 2, 55, 1, 34, 32, 22, 6]
index = 3
var = [*range(index, len(arr))] + [*range(0, index)]
nums = [3, 3]
tar = 6


class Solution(object):
    def romanToInt(self, s=str):
        roman_dict = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1}

        total = 0
        prev_value = 0
        for element in s[::-1]:
            value = roman_dict[element]
            total += value
            if value < prev_value:
                total -= 2 * value
                print(f"total after minus: {total}")

            prev_value = value

        return total


s = Solution()
print(s.romanToInt(''))
