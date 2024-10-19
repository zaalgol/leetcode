from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
        
        
class Solution:
    def isPalindrome(self, head) -> bool:
        count = 0
        temp = head
        while temp:
            temp = temp.next
            count +=1
        if count == 1:
            return True
        half = int(count/2)
        
        half_pointer = head
        for _ in range(half):
            half_pointer = half_pointer.next
            
        new_head = head
        while head.next != half_pointer:
            temp = head.next
            head.next = head.next.next
            temp.next = new_head
            new_head = temp
        
        temp = new_head
        if count % 2 == 0:
            temp2 = half_pointer
        else:
            temp2 = half_pointer.next
        while temp2:
            if temp.val != temp2.val:
                return False
            temp = temp.next
            temp2 = temp2.next
            
        return True
    
    def maxSubArray(self, nums) -> int:
        currentMaxi = maxi = nums[0]
        for i in nums[1:]:
            currentMaxi += i
            if currentMaxi < i:
                currentMaxi = i
            if currentMaxi > maxi:
                maxi = currentMaxi
        return maxi
    
    def __init__(self, nums):
        self.nums = nums

    def __init__(self):
        pass
        
    def reset(self):
        return self.nums
        
    def shuffle(self):
        import random
        nums = []
        lenn = len(self.nums)
        for i in range(lenn):
            j = random.randint(0, lenn-1)
            nums[i] = self.nums[j]
        return nums
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        temp = head
        
        head_new = Node(head.val)
        temp_new = head_new

        d_original_to_new = {head: head_new}
        while temp.next:
            temp_new.next = Node(temp.next.val)
            d_original_to_new[temp.next] = temp_new.next
            temp_new = temp_new.next
            temp = temp.next

        temp = head
        temp_new = head_new
        while temp:
            if temp.random in d_original_to_new:
                temp_new.random = d_original_to_new[temp.random]
            temp_new = temp_new.next
            temp = temp.next
        
        return head_new
    
    def reverseBetween(self, head, left: int, right: int):
        temp = head
        i = 1
        before_left = None
        after_right = None
        right_node = None
        left_node = None
        while i <= right:
            if i == left-1 :
                before_left = temp
            if i == left :
                left_node = temp    
            if i == right:
                right_node = temp
                after_right = temp.next
                break
            temp = temp.next
            i+=1


        new_head = left_node
        while left_node.next and left_node.next != after_right:
            temp = left_node.next
            left_node.next = left_node.next.next
            temp.next = new_head
            new_head = temp

        if before_left:
            before_left.next = new_head
        else:
            head = new_head
        
        if after_right:
            left_node.next = after_right

        return head
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if n == 1:
        #     return head.next
        temp = head
        temp2 = head
        i = -n
        while temp.next:
            temp = temp.next
            if i >=0:
                temp2 = temp2.next
            i +=1
        temp2.next = temp2.next.next
        return head
      
    
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        new_head = None
        new_temp = new_head
        while temp:
            if temp.next and temp.val == temp.next.val:
                val = temp.val
                while temp and temp.val == val:
                    temp = temp.next
                    
            else:
                if new_head:
                    new_temp.next = ListNode(temp.val)
                    new_temp = new_temp.next
                else:
                    new_head = ListNode(temp.val)
                    new_temp = new_head
                temp = temp.next
        return new_head
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not k or not head:
            return head
        temp = head
        i=1
        while temp.next:
            i +=1
            temp = temp.next
        k = k% i
        if k == 0:
            return head
        last = temp
        temp = head
       
        # kn = -k
        for j in range(i-k-1):
            temp = temp.next
        last.next = head
        new_temp = temp.next
        temp.next = None
        return new_temp
    
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        small_list= None
        small_list_head= None
        big_list = None
        big_list_head = None
        temp = head
        while temp:
            if temp.val < x:
                if small_list:
                    small_list.next = ListNode(temp.val)
                    small_list = small_list.next 
                else:
                    small_list = ListNode(temp.val)
                    small_list_head= small_list
            else:
                if big_list:
                    big_list.next = ListNode(temp.val)
                    big_list = big_list.next 
                else:
                    big_list = ListNode(temp.val)
                    big_list_head = big_list
            temp = temp.next
        if not big_list:
            return small_list_head
        if not small_list:
            return big_list_head
        small_list.next = big_list_head
        return small_list_head
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        temp = head
        temp2 = head
        i = -n
        while temp.next:
            temp = temp.next
            if i >=0:
                temp2 = temp2.next
            i +=1
        if i == -1: # edge case like n=2. list is [4,5]
            return temp2.next
        temp2.next = temp2.next.next
        
        return head
        
            
            
        
if __name__ == '__main__':  
    solution = Solution()  

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    solution.removeNthFromEnd(node1, 2)

    node22 = ListNode(2)
    node5 = ListNode(5)
    node5.next = node22
    node2 = ListNode(2)
    node2.next = node5
    node3 = ListNode(3)
    node3.next = node2
    node4 = ListNode(4)
    node4.next = node3
    node1 = ListNode(1)
    node1.next = node4
    solution.partition(node1, 3)

   


    node5 = ListNode(5)
    node4 = ListNode(4)
    node4.next = node5
    node3 = ListNode(3)
    node3.next = node4
    node2 = ListNode(2)
    node2.next = node3
    node1 = ListNode(1)
    node1.next = node2  
    solution.rotateRight(node1, 2)

    node33 = ListNode(3)
    node3 = ListNode(3)
    node3.next = node33
    node2 = ListNode(2)
    node2.next = node3
    node1 = ListNode(1)
    node1.next = node2
    solution.deleteDuplicates(node1)


    node2 = ListNode(2)
    node1 = ListNode(1)
    node1.next = node2
    solution.removeNthFromEnd(node1, 1)
    node5 = ListNode(5)
    node4 = ListNode(4)
    node4.next = node5
    node3 = ListNode(3)
    node3.next = node4
    node2 = ListNode(2)
    node2.next = node3
    node1 = ListNode(1)
    node1.next = node2
    solution.removeNthFromEnd(node1, 2)


    node5 = ListNode(5)
    node3 = ListNode(3)
    node3.next = node5
    solution.reverseBetween(node3, 1, 2)
    node5 = ListNode(5)
    node4 = ListNode(4)
    node4.next = node5
    node3 = ListNode(3)
    node3.next = node4
    node2 = ListNode(2)
    node2.next = node3
    node1 = ListNode(1)
    node1.next = node2
    solution.reverseBetween(node1, 2, 4)


    node7 = Node(7)
    node13 = Node(13)
    node11 = Node(11)
    node10 = Node(10)
    node1 = Node(1)
    node7.next = node13
    node13.next =node11
    node13.random =node7
    node11.next =node10
    node11.random =node1
    node10.next =node1
    node10.random =node11
    node1.random= node7
    solution.copyRandomList(node7)






    solution = Solution([1, 2, 3]) 
    solution.shuffle()
    solution.reset()
    
    solution.maxSubArray([5,4,-1,7,8])
    
    
    head = ListNode(1)
    print(solution.isPalindrome(head))
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
    print(solution.isPalindrome(head))
    head = ListNode(1, ListNode(2,  ListNode(2, ListNode(1))))
    print(solution.isPalindrome(head))
    head = ListNode(1, ListNode(3, ListNode(3, ListNode(2, ListNode(1)))))
    print(solution.isPalindrome(head))
    head = ListNode(1, ListNode(2,  ListNode(3, ListNode(1))))
    print(solution.isPalindrome(head))
    
    t =0
    