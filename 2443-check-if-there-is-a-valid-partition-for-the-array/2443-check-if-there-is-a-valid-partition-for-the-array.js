/**
 * @param {number[]} nums
 * @return {boolean}
 */
var validPartition = function(arr) {
    dp = new Array(arr.length+1).fill(false)
    dp[0] = true
    for(let i = 1;i<dp.length;i++){
      if(i>=2){
        if(arr[i-1] == arr[i-2]){
          dp[i] = dp[i-2] || dp[i]
        }
      }
      if(i>=3){
        if((arr[i-1]==arr[i-2] && arr[i-2] == arr[i-3]) || (arr[i-1]-arr[i-2]==1 && arr[i-2] - arr[i-3] == 1)){
          dp[i] = dp[i-3] || dp[i]
        }
      }
    }
    return dp[dp.length - 1]
};