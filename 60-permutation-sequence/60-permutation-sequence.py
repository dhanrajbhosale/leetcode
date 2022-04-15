import math
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        numbers = range(1, n+1)
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])

        return permutation

# JAVA SOLUTION 
# public class Solution {
# public String getPermutation(int n, int k) {
#     List<Integer> numbers = new ArrayList<>();
#     int[] factorial = new int[n+1];
#     StringBuilder sb = new StringBuilder();
    
#     // create an array of factorial lookup
#     int sum = 1;
#     factorial[0] = 1;
#     for(int i=1; i<=n; i++){
#         sum *= i;
#         factorial[i] = sum;
#     }
#     // factorial[] = {1, 1, 2, 6, 24, ... n!}
    
#     // create a list of numbers to get indices
#     for(int i=1; i<=n; i++){
#         numbers.add(i);
#     }
#     // numbers = {1, 2, 3, 4}
#     k--;
    
#     for(int i = 1; i <= n; i++){
#         int index = k/factorial[n-i];
#         sb.append(String.valueOf(numbers.get(index)));
#         numbers.remove(index); 
#         k=k%factorial[n-i];
#     }
    
#     return String.valueOf(sb);
# }
# }