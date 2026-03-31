func isAnagram(s string, t string) bool {
	if len(s) != len(t){
		return false
	}

	a := make(map[rune]int)
	b := make(map[rune]int)

	frequency := func (s string, freq map[rune]int) map[rune]int{
		for _, value := range s{
			freq[value]++
		}
		return freq
	}

	a = frequency(s, a)
	b = frequency(t, b)

	for k, v1 := range a{
		if v2, ok := b[k]; ok != true || (v2 != v1){
			return false
		}
	}

	return true
}
