/**
 * @param {number} n
 * @param {number[][]} roads
 * @return {number}
 */
var maximalNetworkRank = function(n, roads) {
  if(roads.length == 0){
    return 0
  }
    mp = new Map()
    st = new Map()
    for(let i = 0; i<roads.length;i++){
      if(mp[roads[i][0]]){
        mp[roads[i][0]] += 1
      }
      else {
        mp[roads[i][0]] = 1
      }
      if(mp[roads[i][1]]){
        mp[roads[i][1]] += 1
      }
      else {
        mp[roads[i][1]] = 1
      }
      st[JSON.stringify([roads[i][0],roads[i][1]])] = 1
    }
    let mx = 0
    for(let i = 0;i<n-1;i++){
      for(let j = i+1;j<n;j++){
        if(mp[i] && mp[j]){
        let val = mp[i] + mp[j]
        if(st[JSON.stringify([i,j])] || st[JSON.stringify([j,i])]){
          val -= 1
        }
        mx = Math.max(mx,val)
        }
      }
    }
    return mx
};