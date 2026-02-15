class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        Map<Character,Integer> m=new HashMap<>();
        int ans=0;
        for(int i=0;i<stones.length();i++)
        {
            m.put(stones.charAt(i),m.getOrDefault(stones.charAt(i),0)+1);
        }
        for(int i=0;i<jewels.length();i++)
        {
            if(m.containsKey(jewels.charAt(i)))
            {
                ans+=m.get(jewels.charAt(i));
            }
        }
        return ans;
    }
}