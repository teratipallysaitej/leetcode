func helper(v int, z map[int][]int, visited []bool, recStack []bool) bool {
	if visited[v] {
		return false
	}
	if recStack[v] {
		return true
	}
	recStack[v] = true
	if len(z[v]) > 0 {
		for _, i := range z[v] {
			if helper(i, z, visited, recStack) {
				return true
			}
		}
	}
	visited[v] = true
	recStack[v] = false // reset the recursion stack before exiting
	return false
}

func canFinish(numCourses int, prerequisites [][]int) bool {
	visited := make([]bool, numCourses)
	recStack := make([]bool, numCourses)
	z := make(map[int][]int)
	for i := 0; i < len(prerequisites); i++ {
		z[prerequisites[i][0]] = append(z[prerequisites[i][0]], prerequisites[i][1])
	}
	for v := 0; v < numCourses; v++ {
		if helper(v, z, visited, recStack) {
			return false
		}
	}
	return true
}