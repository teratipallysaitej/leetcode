func findMin(nums []int) int {
    st := 0
    en := len(nums) - 1
    for st < en {
        if nums[st] <= nums[en] {
            break
        }
        mid := st + (en-st)/2
        if nums[st] <= nums[mid] {
            st = mid + 1
        } else {
            en = mid
        }
    }
    return nums[st]
}