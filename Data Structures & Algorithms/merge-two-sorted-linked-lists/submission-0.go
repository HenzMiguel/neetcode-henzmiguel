/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    
	a, b := list1, list2
	head := &ListNode{}
	res := head

	for a != nil && b != nil{
		if a.Val > b.Val{
			res.Next = b
			b = b.Next
		}else{
			res.Next = a
			a = a.Next
		}
		res = res.Next
	}

	for a != nil{
		res.Next = a
		a = a.Next
		res = res.Next
	}

	for b != nil{
		res.Next = b
		b = b.Next
		res = res.Next
	}

	return head.Next
}
