class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = defaultdict(int)

        for integer in nums:
            my_dict[integer] += 1

        sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
        print(sorted_dict)
        res = []
        for idx, key in enumerate(sorted_dict):
            if idx == k:
                break
            res.append(key)
            
        return res
