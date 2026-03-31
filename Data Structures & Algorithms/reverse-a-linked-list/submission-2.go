/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverseList(head *ListNode) *ListNode {
    if head == nil{
        return nil
    }

    node := head
	var prev *ListNode
    var temp *ListNode

	for node != nil{
		temp = node.Next
		node.Next = prev
		prev = node
		node = temp
	}
	return prev
}
