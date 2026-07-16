class Solution {
    public void sortColors(int[] nums) {
        int left = 0;
        int mid = 0;
        int right=nums.length-1;

        while(mid<=right){
            if(nums[mid]==1){
                mid+=1;
            }
            else if(nums[mid]==2){
                int temp = nums[right];
                nums[right]=2;
                nums[mid]=temp;
                right-=1;
            }
            else if(nums[mid]==0){
                int temp = nums[left];
                nums[left]=0;
                nums[mid]=temp;
                left+=1;
                mid+=1;
            }
        }

    }
}