func hasDuplicate(nums []int) bool {
    isin := make(map[int]bool)
    for _ , num := range nums{
        if _ , ok := isin[num]; ok == true{
            return true
        }
        isin[num] = true
    }
    
    return false
}
