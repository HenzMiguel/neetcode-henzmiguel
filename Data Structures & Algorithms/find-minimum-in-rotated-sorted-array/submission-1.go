func findMin(nums []int) int {

	l := 0
	r := len(nums) - 1
	var m int
	min := math.MaxInt
	for l <= r {
		if nums[l] < nums[r]{
			if min > nums[l]{
				min = nums[l]
				break
			}
		}

		m = l + (r - l) / 2
		fmt.Println(nums[l], nums[m], nums[r])
		if nums[l] <= nums[m]{
			l = m + 1
		}else{
			r = m - 1
		}
		
		if min > nums[m]{
			min = nums[m]
		}
	}
	return min
}
