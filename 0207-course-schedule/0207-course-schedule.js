var canFinish = function(numCourses, prerequisites) {
  const helper = (v, z) => {
    if (visited[v]) {
      return false;
    }
    if (recStack[v]) {
      return true;
    }
    recStack[v] = true;
    const li = z.get(v) || [];
    for(let i = 0; i < li.length; i++) {
      if(helper(li[i], z)) {
        return true;
      }
    }
    visited[v] = true;
    recStack[v] = false;
    return false;
  }
  const visited = new Array(numCourses).fill(false);
  const recStack = new Array(numCourses).fill(false);
  const z = new Map();
  for(const [x, y] of prerequisites) {
    if(z.has(x)) {
      z.get(x).push(y);
    } else {
      z.set(x, [y]);
    }
  }
  for(let v = 0; v < numCourses; v++) {
    if (helper(v, z)) {
      return false;
    }
  }
  return true;
};
