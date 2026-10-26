class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int l=0;
        int r=0;
        int avg=0;
        int ans=Integer.MIN_VALUE;
        while(r<nums.length){
            avg+=nums[r];
            if((r-l+1)==k){
                ans=Math.max(avg,ans);
                avg-=nums[l];
                l++;
            }
            r++;
        }
        return (double) ans/k;
    }
}