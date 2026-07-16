import java.util.*;
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Map<Integer, Integer> map= new HashMap<>();
        // map.put(0,0);
        Set<List<Integer>> ans = new HashSet<>();
        Arrays.sort(nums);
        // for(int i=0;i<nums.length;i++){
        //     for(int j=i+1;j<nums.length;j++){
        //         for(int k=j+1;k<nums.length;k++){
        //             if(nums[i]+nums[j]+nums[k]==0){
        //                 List<Integer> temp = new ArrayList<>();
        //                 temp.add(nums[i]);
        //                 temp.add(nums[j]);
        //                 temp.add(nums[k]);
        //                 Collections.sort(temp);
        //                 ans.add(temp);
        //             }
        //         }

        //     }

        // }

        int i=0;
        while(i<nums.length-2){
            int j=i+1;
            int k=nums.length-1;
            while(j<k){
                if(nums[i]+nums[j]+nums[k]==0){
                    List<Integer> temp = new ArrayList<>();
                    temp.add(nums[i]);
                    temp.add(nums[j]);
                    temp.add(nums[k]);
                    Collections.sort(temp);
                    ans.add(temp);
                    j++;
                    k--;
                }
                else if(nums[i]+nums[j]+nums[k]>0){
                    k--;
                }else{
                    j++;
                }
            }
            i++;
        }

        return new ArrayList<>(ans);
        // return new int[]{0,0};
        // if(map.containsKey(nums[i]+nums[j])){
        //             return new int[]{map.get(nums[i]+nums[j]), i, j};
        //         }
        //         map.put(target-(nums[i]+nums[j]), i);
    }
}