/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let ans = 0;
    for(let i=1; i<=nums.length; i++){
        ans ^= i
    }
    for(let i of nums){
        ans ^= i
    }
    return ans
};