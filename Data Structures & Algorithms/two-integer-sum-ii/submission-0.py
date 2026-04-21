class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}
        for i, n in enumerate(numbers):
            if n in map:
                return [map[n]+1,i+1]
            else:
                map[target-n] = i