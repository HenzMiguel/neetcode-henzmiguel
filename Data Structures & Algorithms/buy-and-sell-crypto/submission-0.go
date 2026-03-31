func maxProfit(prices []int) int {

	left := 0
	max := 0
	for r:=1; r < len(prices); r++{
		diference := prices[r] - prices[left]
		if diference < 0{
			left = r
		}
		if diference > max{
			max = diference
		}
	}
	return max
}
