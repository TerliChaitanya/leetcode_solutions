class Solution {
    public int[] replaceElements(int[] arr) {
       int max=arr[arr.length-1];
       arr[arr.length-1]=-1;
       for(int j=arr.length-2;j>=0;j--)
       {
        int temp=arr[j];
        arr[j]=max;
        max=Math.max(max,temp);
       }return arr;
    }
}