# 두 수의 합
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans = [i, j]
        return ans
    
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums): # 순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력으로 받았을 때, 인덱스와 값을 포함하여 리턴
            temp = target - n
            if temp in nums[i + 1:]:
                return [nums.index(n), nums[i+1:].index(temp)+(i+1)]
            
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i # 키와 값 바꿔서 저장
        
        for i, num in enumerate(nums):
            if target-num in nums_map and i != nums_map[target - num]: # i != nums_map[target - num]은 같은 숫자를 두 번 사용하지 않도록 보장
                return [i, nums_map[target-num]]
    
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            if target-num in nums_map:
                return [nums_map[target-num], i]
            nums_map[num] = i