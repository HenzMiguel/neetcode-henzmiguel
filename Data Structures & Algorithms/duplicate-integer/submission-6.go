func hasDuplicate(nums []int) bool {
    hash := make(map[int]bool)

    for _, value := range nums{
        if _, ok := hash[value]; ok == true{
            return true
        }
        hash[value] = true
    }
    return false
}
