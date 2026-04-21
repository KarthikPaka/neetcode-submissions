class Solution:
    def trap(self, height: List[int]) -> int:
        peakSeenLeft = [0] * len(height)
        peakSeenRight = [0] * len(height)
        total = 0

        leftPointer = 0
        rightPointer = len(height) - 1
        prevPeak = 0

        while leftPointer <= rightPointer:
            if prevPeak < height[leftPointer]:
                peakSeenLeft[leftPointer] = prevPeak = height[leftPointer]
            else:
                peakSeenLeft[leftPointer] = prevPeak

            leftPointer += 1
        
        leftPointer = prevPeak = 0
        while leftPointer <= rightPointer:
            if prevPeak < height[rightPointer]:
                peakSeenRight[rightPointer] = prevPeak = height[rightPointer]
            else:
                peakSeenRight[rightPointer] = prevPeak

            rightPointer -= 1

        water = [0] * len(height)
        puddle = 0
        for i in range(len(height)):
            puddle = min(peakSeenLeft[i], peakSeenRight[i]) - height[i]
            water[i] = puddle
            total += puddle

        print(peakSeenLeft)
        print(peakSeenRight)
        print(water)
        return total