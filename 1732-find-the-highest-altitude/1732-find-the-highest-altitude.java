class Solution {
    public int largestAltitude(int[] gain) {
        int alt=0;
        int max =0;
        for(int val:gain){
            alt=alt+val;
            if(max<alt)
            {
                max=alt;
            }
        }
        return max;
    }
}