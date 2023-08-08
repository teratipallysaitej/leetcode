/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let st=0, en = nums.length - 1;
    while(st<=en){
        let mid = Math.floor(st + (en-st)/2);
        if(nums[mid] == target){
            return mid
        }
        if(nums[st] <= nums[mid]){
            if(target >= nums[st] && target < nums[mid]){
                        en = mid - 1}
                else{
                        st = mid + 1}}
        else{
            if(target > nums[mid] && target <= nums[en]){
                st = mid + 1
            }
            else{
                en = mid - 1
            }
        }
    }
    return nums[st]==target ? st : -1 ;
};