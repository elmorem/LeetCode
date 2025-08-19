/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    let currentSum = 0;
    for (let i =0; i<k; i++) {
        currentSum += nums[i]
    }
    let maxSum = currentSum;
    for (let i = k; i <nums.length; i++) {
        currentSum = currentSum - nums[i-k] + nums[i];
        maxSum = Math.max(maxSum, currentSum);
    }
    return maxSum/k
};