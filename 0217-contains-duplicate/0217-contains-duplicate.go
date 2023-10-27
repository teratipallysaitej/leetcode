func containsDuplicate(nums []int) bool {
    mp := make(map[int]int)

    for i:=0;i<len(nums);i++ {
        _, present := mp[nums[i]]
        if present {
            return true
        }
        mp[nums[i]] = 1
    }  
    return false 
}