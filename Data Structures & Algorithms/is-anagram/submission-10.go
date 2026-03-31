func isAnagram(s string, t string) bool {
    if len(s) != len(t){
        return false
    }
    
    a := make(map[rune]int)
    b := make(map[rune]int)

    for _, v := range s{
        a[v]++
    }

     for _, v := range t{
        b[v]++
    }

    for i, v := range a{
        if v2, ok := b[i]; ok != true || v2 != v{
            return false
        }
    }
    return true
}
