/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    mx = Math.max(...candies)
    res = []
    console.log(mx)
    for(let i = 0;i<candies.length;i++){
        if(candies[i]+extraCandies>=mx){
            res.push(true)
        }
        else{
            res.push(false)
        }
    }
    return res
};