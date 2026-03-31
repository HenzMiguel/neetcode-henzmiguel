def recurse(n, cache):
	if n == 0:
		return 1
	elif n < 0:
		return 0

	if n in cache:
		return cache[n]

	cache[n - 1] = recurse(n - 1, cache)
	cache[n - 2] = recurse(n - 2, cache)

	cache[n] = cache[n - 1] + cache[n - 2]

	return cache[n]


class Solution:
    def climbStairs(self, n: int) -> int:
        return recurse(n, {})