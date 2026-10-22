class Solution {
    public int maxNumberOfBalloons(String text) {
        int[] count=new int[26];
        int result=Integer.MAX_VALUE;
        for(char ch: text.toCharArray()){
            count[ch-'a']++;
        }
        count['l'-'a']/=2;
        count['o'-'a']/=2;
        String balloon="balon";
        for (char ch:balloon.toCharArray()){
            result=Math.min(result,count[ch-'a']);
        }
        return result;
    }
}