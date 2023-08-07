/**
 * @param {string} s
 * @return {string}
 */
var removeStars = function(s) {
    st = []
    for(let i = 0;i<s.length;i++){
        if(s[i] =='*'){
            st.pop()
            }
         else{
             st.push(s[i])
         }
        }
        return st.join('')
};