/*
Put the same array on itself
*/
func getConcatenation(nums []int) []int {
	n := len(nums)
	res := make([]int, 0, 2*n)
	res = append(res, nums...)
	return append(res, nums...)
}
