class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem = {}
        for i in range(len(nums)):
            rem[target - nums[i]] = i

        
        for i in range(len(nums)):
            if nums[i] in rem:
                if rem[nums[i]]< i:
                    return [rem[nums[i]] , i]
                elif rem[nums[i]] == i:
                    continue
                else:
                    return[i, rem[nums[i]]]


            