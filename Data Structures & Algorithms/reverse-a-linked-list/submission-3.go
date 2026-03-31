/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverse(curr, prev *ListNode) *ListNode{
		if curr == nil{
			return prev
		}else{
			next := curr.Next
			curr.Next = prev
			return reverse(next, curr)
		}
	}

func reverseList(head *ListNode) *ListNode {
	return reverse(head, nil)
}
