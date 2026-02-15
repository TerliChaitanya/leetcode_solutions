class Solution {
    public int numIdenticalPairs(int[] nums) {
        HashMap <Integer , Integer> hash=new HashMap<>();
        int ans=0;
        for(int i=0;i<nums.length;i++)
        {
            if(hash.containsKey(nums[i]))
            {
                ans+=hash.get(nums[i]);
            }
            hash.put(nums[i],hash.getOrDefault(nums[i],0)+1);
            
        }
        return ans;
    }
}