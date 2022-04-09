// The key is, think 'result' as a list to save the numbers, so everytime we get the last digit of 'n', just shift 'result' to the left and use '|' to store the last digit of 'n'.
 public class Solution {
        // you need treat n as an unsigned value
        public int reverseBits(int n) {
            int result = 0;
            for (int i = 0;i<32;i++){
                int end = n & 1;
                n >>= 1;
                result <<=1;
                result |= end;
            }
            return result;
        }
    }