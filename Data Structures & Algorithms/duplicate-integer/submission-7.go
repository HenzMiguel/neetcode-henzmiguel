func hasDuplicate(nums []int) bool {
    isin := make(map[int]bool)

    for _, num := range nums{
        if isin[num]{
            return true
        }
        isin[num] = true
    }
    return false
}
