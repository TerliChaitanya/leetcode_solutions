class Solution {
    public int maxArea(int[] height) {
        int right=height.length-1;
        int left=0;
        int max_area=0;
        while(left<right)
        {
            int min_height=Math.min(height[left],height[right]);
            max_area=Math.max(max_area,min_height*(right-left));
            if(height[right]<height[left])
            {
                right--;
            }
            else
            {
                left++;
            }
        }
        return max_area;
    }
}