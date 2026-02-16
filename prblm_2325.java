class Solution {
    public String decodeMessage(String key, String message) {
        HashMap<Character,Character> hm=new HashMap<>();
        int a=97;
        String ans="";
        hm.put(' ',' ');
        for(char c:key.toCharArray())
        {
            if(!hm.containsKey(c))
            {
                hm.put(c,(char)a);
                a++;
            }
        }
        for(a=0;a<message.length();a++)
        {
            ans+=""+hm.get(message.charAt(a));
        }
        return ans;
    }
}