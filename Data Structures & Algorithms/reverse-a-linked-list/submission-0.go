/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverseList(head *ListNode) *ListNode {
    
	node := head
	var prev *ListNode

	for node != nil{
		temp := node.Next
		node.Next = prev
		prev = node
		node = temp
	}
	return prev
}
