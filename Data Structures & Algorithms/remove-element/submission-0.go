/*
remove val int from nums
return the numbers of elements from remaining array
*/

func removeElement(nums []int, val int) int {
    copied := []int{}

	for i := range nums{
		if nums[i] != val{
			copied = append(copied, nums[i])
		}
	}
	copy(nums, copied)
	return len(copied)
}
