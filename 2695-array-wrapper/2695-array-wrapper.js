/**
 * @param {number[]} nums
 */
var ArrayWrapper = function(nums) {
    this.nums = nums;
};

/**
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function() {
    return this.nums.reduce((sum, num) => sum + num, 0);
};

/**
 * @return {string}
 */
ArrayWrapper.prototype.toString = function() {
    return "[" + this.nums.join(",") + "]";
};