type MinStack struct {
	min []int
	stack []int
}

func Constructor() MinStack {
	return MinStack{make([]int, 0 , 1), make([]int, 0, 1),}
}
func less (min []int, b int) []int {
	if len(min) == 0{
		return append(min, b)
	}

	if min[len(min) - 1] > b{
		return append(min, b)
	}
	fmt.Println(min)
	return append(min, min[len(min) - 1])
}

func (this *MinStack) Push(val int) {
	this.min = less(this.min, val)
	this.stack = append(this.stack, val)
}

func (this *MinStack) Pop() {
	this.stack = this.stack[:len(this.stack) - 1]
	this.min = this.min[:len(this.min) - 1]
}

func (this *MinStack) Top() int {
	return this.stack[len(this.stack) - 1]	
}

func (this *MinStack) GetMin() int {
	return this.min[len(this.stack) - 1]
}
