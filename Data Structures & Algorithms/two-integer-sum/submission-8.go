func twoSum(nums []int, target int) []int {
    m := make(map[int]int)

    for i := 0; i<len(nums); i++ {
        curr := nums[i]
        if _, ok := m[curr]; ok {
            return []int{m[curr], i}
        }

        m[target - curr] = i
    }
    return []int{}
}
