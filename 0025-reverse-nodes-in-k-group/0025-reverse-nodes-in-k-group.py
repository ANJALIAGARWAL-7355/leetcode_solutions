class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            # Check if there are k nodes left
            kth = prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            # Save the node after the group
            next_group = kth.next

            # Reverse the k nodes
            curr = prev.next
            prev_node = next_group

            while curr != next_group:
                temp = curr.next
                curr.next = prev_node
                prev_node = curr
                curr = temp

            # Connect previous part to reversed group
            temp = prev.next
            prev.next = kth
            prev = temp