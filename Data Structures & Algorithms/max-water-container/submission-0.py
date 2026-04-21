class Solution:

    # input = heights = [1,7,2,5,4,7,3,6]

    #area = height * weight
    #we want max area

    #start from the ends
    #save the max
    #as you go into middle if you have a very large height that passes the prev max
    #then you can update



    def maxArea(self, heights: List[int]) -> int:
        if heights == None or len(heights) < 2:
            return 0
        p1 = 0
        p2 = len(heights) - 1

        maxArea = 0

        while (p1 < p2):
            currArea = min(heights[p1], heights[p2])* (p2 - p1)
            if (currArea > maxArea):
                maxArea = currArea
            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1
        

        return maxArea
        