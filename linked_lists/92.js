/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
var reverseBetween = function(head, left, right) {
    if (!head || !head.next || left === right){
        return head;
    }
    const dummy = new ListNode(0);
    dummy.next = head;

    let prev = dummy;
    for (let i =0; i < left -1; i++) {
        prev = prev.next
    }
    let start = prev.next;
    let curr = start;
    let reversePrev = null;
    for (let i = 0; i< right -left+1; i++) {
        const next = curr.next;
        curr.next = reversePrev;
        reversePrev = curr;
        curr = next;
    }
    prev.next = reversePrev;
    start.next = curr;
    return dummy.next

};