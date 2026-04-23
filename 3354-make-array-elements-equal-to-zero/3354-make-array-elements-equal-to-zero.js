/**
 * @param {number[]} nums
 * @return {number}
 */
var countValidSelections = function(nums) {
    let n = nums.length;
    function tryToZero(start, direction){
        const arr = [...nums];
        let curr = start;
        let dir = direction;
        while(curr>=0 && curr<n){
            if(arr[curr] == 0){
                curr += dir;
            }
            else {
                arr[curr] -= 1
                dir = -dir
                curr += dir;
            }
        }
        return arr.every(x => x === 0);   
    }
    let validCount = 0;
    for(let i=0;i<n;i++){
        if(nums[i] == 0){
            if(tryToZero(i, 1)) validCount++; //right move
            if(tryToZero(i, -1)) validCount++; //left move
        }   
    }
    return validCount;
};