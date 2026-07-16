class Solution {
    public int majorityElement(int[] nums) {
        int element = nums[0];
        int count = 1;
        for(int i=1;i<nums.length;i++){
            if(count==0){
                count+=1;
                element = nums[i];
            }
            else if(nums[i]==element) count+=1;
            else if(nums[i]!=element) count-=1;
        }
        return element;
    }
}