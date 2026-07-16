import java.util.*;
class Solution {
    public void nextPermutation(int[] nums) {
        int breakPoint = -1;
        for(int i=nums.length-2;i>=0;i--){
            if(nums[i+1] <= nums[i]) continue;
            breakPoint = i;
            break;
        }
        System.out.println(breakPoint);
        if(breakPoint==-1){
            Arrays.sort(nums); 
            return;
        }

        for(int i=nums.length-1;i>=0;i--){
            if(nums[i]>nums[breakPoint]){
                int temp = nums[breakPoint];
                nums[breakPoint] = nums[i];
                nums[i]=temp;
                break;
            }
        }


        int temp[] = new int[nums.length-1-breakPoint];
        for(int i=breakPoint+1;i<nums.length;i++){
            temp[i-1-breakPoint] = nums[i];
        }
        Arrays.sort(temp);
        for(int i=breakPoint+1;i<nums.length;i++){
           nums[i]=temp[i-1-breakPoint];
        }
    }
}