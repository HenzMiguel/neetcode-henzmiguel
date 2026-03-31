/*
i != j
only one answer. There is always an answer
return answer with smaller index first (resolved with for loop)
*/
func twoSum(nums []int, target int) []int {
    
    hash := make(map[int]int)

    for i:=0; i < len(nums); i++{
        if val, ok := hash[nums[i]]; ok{
            return []int{val, i}
        }
        hash[target - nums[i]] = i
    }
    return []int{0,0}
}
