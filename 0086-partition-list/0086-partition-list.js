/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} x
 * @return {ListNode}
 */
var partition = function(head, x) {
    l = left = new ListNode(-1)
    r = right = new ListNode(-1)
    curr = head
    l_p = null
    r_p = null
    while(curr){
        if(curr.val < x){
            l_p = left
            left.next = curr
            left = left.next
            curr = curr.next
            left.next = null
        }else{
            r_p = right
            right.next = curr
            right = right.next
            curr = curr.next
            right.next = null
        }
    }
    left.next = r.next
    r.next = null
    l = l.next 
    return l
};