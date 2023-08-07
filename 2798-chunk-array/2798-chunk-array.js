/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    res = []
    let i = 0
    let n = arr.length
    while(i<n){
        j = 0
        new_arr = []
        for(let j = 0;j<size;j++){
            if(j==size){
                break
            }
            if(i>=n){
                break
            }
            new_arr.push(arr[i])
            i += 1
        }
        res.push(new_arr)
    }
return res
};