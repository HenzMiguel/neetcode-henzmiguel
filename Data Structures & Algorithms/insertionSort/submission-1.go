// Definition for a pair.
// type Pair struct {
//     Key   int
//     Value string
// }

func insertionSort(pairs []Pair) [][]Pair {
	res := make([][]Pair,0,0)
	if pairs == nil{
		return res
	}
	copied := make([]Pair, len(pairs))
	copy(copied, pairs)
	res = append(res, copied)

	for i := 1; i < len(pairs); i++{
		j := i
		for j > 0 && pairs[j].Key < pairs[j - 1].Key {
			pairs[j], pairs[j - 1] = pairs[j - 1], pairs[j]
			j--
		}
		list := make([]Pair, len(pairs))
		copy(list, pairs)
		res = append(res, list)
	}
	return res
}
