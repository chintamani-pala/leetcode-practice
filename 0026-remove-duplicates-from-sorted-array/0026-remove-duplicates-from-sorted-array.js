/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let p = 0;
    for(let i=1;i<nums.length;i++){
        if(nums[p] == nums[i]) continue
        nums[p+1] = nums[i];
        p++;
    }
    return p+1
};