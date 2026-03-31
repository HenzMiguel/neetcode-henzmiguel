/*
abrir e fechar com o mesmo tipo.
abrir e fechar na ordem correta
todo fechado tem um aberto.

usar um stack. go slice
*/

func isValid(s string) bool {
    stack := make([]rune, 0, 1000)
	verify := map[rune]rune {
		')':'(',
		']': '[',
		'}': '{',
	}

	for _, c := range s{
		if len(stack) > 0 && verify[c] == stack[len(stack) - 1]{
			stack = stack[:len(stack) - 1]
		}else{
			stack = append(stack, c)
		}
	}
	
	if len(stack) > 0{
		return false
	}
	return true

}
