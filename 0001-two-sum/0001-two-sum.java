class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map= new HashMap<>();
        // map.put(0,0);
        for(int i=0;i<nums.length;i++){
            if(map.containsKey(nums[i])){
                return new int[]{map.get(nums[i]), i};
            }
            map.put(target-nums[i], i);
        }
        return new int[]{0,0};
    }
}