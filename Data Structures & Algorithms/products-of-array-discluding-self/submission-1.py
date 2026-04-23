class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # In words, we need to multiply all the numbers except the number we are on
        # brute force would be to multiply all and then go back and divide by the number at each inde
        # however we can do this without division by never multiplying by the number at the current index
        # in takes two passes, which i think was necessary even in the brute force approach
        # go right and accumulate the multiples while skipping the one you are on
        # then go left and do the same thing
        # what we mean by skipping is that
        # before you add the current value to your global multiple accumulator
        # first multiply what you have and place it in this spot, then take the value that was there and add it to your accumulator so you can use it for the next spot
        if len(nums) < 2:
            return nums
        acc = nums[0]
        res = [1] * len(nums)


        for i in range(1, len(nums)):
            res[i] = acc # update value at index to be a multiple of everything you have seen so far or 1 for the first index
            acc = acc * nums[i] # update the accumulated multiple to include the current value at this index to use it for the following indicies


        acc = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            res[i] = acc * res[i]
            acc = acc * nums[i]
        
        return res

            # [1,2,4,6]
            # [48,24,12,8]


