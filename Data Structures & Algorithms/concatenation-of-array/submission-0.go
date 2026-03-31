/*
Put the same array on itself
*/
func getConcatenation(nums []int) []int {
    copied := nums
	copied = append(nums, copied...)
	return copied
}
