class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxLength = 0;

        int currentNum = 0;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] == 1){
                currentNum += 1;
            } else {
                currentNum = 0;
            }
            if(currentNum > maxLength) {
                maxLength = currentNum;
            }
        }
        return maxLength;
    }
}