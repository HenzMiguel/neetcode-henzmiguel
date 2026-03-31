/*
Put the same array on itself
*/
func getConcatenation(nums []int) []int {
	return append(nums, nums...)
}
