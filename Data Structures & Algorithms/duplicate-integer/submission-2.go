func hasDuplicate(nums []int) bool {
    isin := make(map[int]bool)
    for _ , num := range nums{
        if _ , ok := isin[num]; ok == false{
            isin[num] = true
        }else{
            return true
        }
    }
    
    return false
}
