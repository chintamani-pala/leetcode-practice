class Solution {
    public int maxSubArray(int[] nums) {
        int sum = 0;
        int max = 0;
        for(int num:nums){
            max =  max<num?max:num;
        }
        for(int num:nums){
            sum+=num;
            max = max>sum?max:sum;
            if(sum<0){
                sum=0;
            }
        }
        return max;
    }
}