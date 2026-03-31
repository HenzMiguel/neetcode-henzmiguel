func recurse(n int, memo map[int]int) int{
	if r, ok := memo[n]; ok{
		return r
	}
	
	if n <= 2 {
		return n
	}

	memo[n] = recurse(n - 1, memo) + recurse(n - 2, memo)
	return memo[n]
}

func climbStairs(n int) int {
	memo := make(map[int]int)
    return recurse(n, memo)
}
