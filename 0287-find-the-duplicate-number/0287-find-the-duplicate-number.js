/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    const trackArr = new Array(nums.length).fill(0);
    for(let i=0;i<nums.length; i++){
        let num = nums[i]
        if(trackArr[num] != -1){
            trackArr[num] = -1;
        }
        else if(trackArr[num] == -1){
            return num
        }
    }
    return nums.length-1
};