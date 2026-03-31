/*
Put the same array on itself
*/
func getConcatenation(nums []int) []int {
	n := len(nums)
	res := make([]int, 2*n)
	copy(res[:n], nums)
	copy(res[n:], nums) 
	return res
}
