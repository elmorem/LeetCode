/**
 * @param {number} n
 * @return {number}
 */
var integerBreak = function(n) {
    if (n <=3 ) {
        return n-1;

    }
    let threes = Math.floor(n/3);
    let remainder = n %3;
    if (remainder === 0) {
        return Math.pow(3, threes);
    } else if (remainder === 1 ) {
        return Math.pow(3, threes-1) *4;

    } else {
        return Math.pow(3, threes) *2
    }
};