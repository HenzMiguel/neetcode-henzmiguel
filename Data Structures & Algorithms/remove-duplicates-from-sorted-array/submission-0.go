func removeDuplicates(nums []int) int {

	prev := -101
	var copied []int
	for i := range nums{
		if nums[i] != prev{
			copied = append(copied, nums[i])
		}
		prev = nums[i]
	}
	copy(nums, copied)
	return len(copied)
}

func remove(nums []int, index int) []int{
	copied := []int{}
	copied = append(copied,nums[:index]...)
	return append(copied, nums[index + 1:]...)
}