class Solution(object):
    def romanToInt(self, s):
        val = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        nums = []
        for ch in s:              
            nums.append(val[ch])

        total = 0
        i = 0
        n = len(nums)

        while i < n:
            if i + 1 < n and nums[i] < nums[i + 1]:
                total += (nums[i + 1] - nums[i])
                i += 2               
            else:
                total += nums[i]
                i += 1                

        return total
