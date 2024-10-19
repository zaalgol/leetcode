# Definition for a binary tree node.
import collections
from queue import Queue
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class BSTIterator: # in order iterator 
  def __init__(self, root: Optional[TreeNode]):
    self.stack = []
    self._pushLeftsUntilNull(root)

  def next(self) -> int:
    root = self.stack.pop()
    self._pushLeftsUntilNull(root.right)
    return root.val

  def hasNext(self) -> bool:
    return self.stack

  def _pushLeftsUntilNull(self, root: Optional[TreeNode]) -> None:
    while root:
      self.stack.append(root)
      root = root.left
    

  
def inOrder(root): # in order traverse
     
    # Set current to root of binary tree
    current = root
     
    # Initialize stack
    stack = []
     
    while True:
         
        # Reach the left most Node of the current Node
        if current is not None:
             
            # Place pointer to a tree node on the stack 
            # before traversing the node's left subtree
            stack.append(current)
         
            current = current.left
         
        # BackTrack from the empty subtree and visit the Node
        # at the top of the stack; however, if the stack is 
        # empty you are done
        elif(stack):
            current = stack.pop()
            print(current.val, end=" ")
         
            # We have visited the node and its left 
            # subtree. Now, it's right subtree's turn
            current = current.right 
 
        else:
            break
     
    print()

class Solution:
    def isSymmetric(self, root):
        
        stackL = []
        curL= root.left
        prevL = None
        
        stackR=[]
        curR= root.right
        prevR = None
        
        while len(stackL) > 0 or (curL and curR):
            if (curL and  curR and curL.val != curR.val) :
                return False
    
            if curL:
                stackL.append(curL)
                curL = curL.left
                stackR.append(curR)
                curR = curR.right
                
            else:
                prevL = stackL.pop()
                curL = prevL.right
                prevR = stackR.pop()
                curR = prevR.left
        if  (curL and not curR) or (not curL and curR):
            return False
        return True
    
    def levelOrder(self, root):
        if not root:
            return []

        ans = []
        q = collections.deque([root])

        while q:
            currLevel = []
            for _ in range(len(q)):
                node = q.popleft()
                currLevel.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(currLevel)

        return ans
    
    temp = None
    def sortedArrayToBST(self, nums):
        return self._sortedArrayToBST_helper(nums, 0, len(nums)-1 )
    
    def _sortedArrayToBST_helper(self, nums, start, end):
        # global temp
        # if start == end:
        #     return TreeNode(nums[start])
        mid = int((start + end) /2)
        node = TreeNode(nums[mid])
        # if node.val == 0:
        #    temp = node
        if mid > start:
            node.left = self._sortedArrayToBST_helper(nums, start, mid-1)
        if end > mid:
            node.right = self._sortedArrayToBST_helper(nums, mid +1, end)
        return node
    
    
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        l=[]
        while i<m and j<n:
            if nums1[i] < nums2[j]:
                l.append(nums1[i])
                i +=1
            else:
                l.append(nums2[j])
                j +=1
        if i<m:
            l.extend(nums1[i:m])
        if j<n:
            l.extend(nums2[j:n])
        nums1[:] = l
        
        
    
    def firstBadVersion(self, n: int) -> int:
        return self.firstBadVersion_helper(1, n)
        
    def firstBadVersion_helper(self, start, end):
        mid = int((start + end)/2)
        if mid >=4:
            if mid == 1 or mid-1 <4:
                return mid
            return self.firstBadVersion_helper(start, mid-1)
        return self.firstBadVersion_helper(mid+1, end)
    
    def levelOrder(self, root):
        if not root:
            return []
        q = Queue(root)
        q.put(root)
        result =[]
        
        while not q.empty():
            level = []
            for _ in range(q.qsize()):
                item = q.get()
                level.append(item.val)
                if item.left: # we check before insert. to not go out of inner loop range
                    q.put(item.left)
                if item.right:
                    q.put(item.right)
            result.append(level)
        return result
    
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        res = []
        q = Queue()
        q.put(root)
        right_start = True
        while not q.empty():
            level =[]
            right_start = not right_start
            for _ in range(q.qsize()):
                item = q.get()
                level.append(item.val)
                if item.left:
                    q.put(item.left)
                if item.right:
                    q.put(item.right)
            if right_start:
                level.reverse()
            res.append(level)
        return res
    
    def flatten_pre_order_to_linked_list_as_left_will_be_null(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        stack = [root]

        while stack:
            root = stack.pop()
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            if stack:
                root.right = stack[-1]
            root.left = None



    def connect(self, root): # every node will also point on a node in the right.
        if not root:
            return root
        q = Queue()
        q.put(root)

        while not q.empty():
            level = []
            for _ in range(q.qsize()):
                item = q.get()
                if level:
                    level[-1].next = item
                level.append(item)
                if item.left: # we check before insert. to not go out of inner loop range
                    q.put(item.left)
                if item.right:
                    q.put(item.right)
        return root
    

    def tree_height_recursive(self, root):
        if not root:
            return 0
        return 1 + max(self.tree_height_recursive(root.left), self.tree_height_recursive(root.right))
    
    def tree_height(self, root):
        if root is None:
            return 0
        
        # Use a queue from the queue library for level-order traversal
        q = Queue()
        q.put(root)
        height = 0
        
        while not q.empty():
            # Number of nodes at the current level
            level_size = q.qsize()
            
            # Process all nodes at the current level
            for _ in range(level_size):
                current_node = q.get()
                
                # Add left and right children to the queue if they exist
                if current_node.left:
                    q.put(current_node.left)
                if current_node.right:
                    q.put(current_node.right)
            
            # Increase height after processing the current level
            height += 1
        
        return height
    
    def serialize(self, root):
        if not root:
            return None
 
        stack = [root]
        l = []
 
        while stack:
            t = stack.pop()
 
            # If current node is NULL, store marker
            if not t:
                l.append("#")
            else:
                # Else, store current node
                # and recur for its children
                l.append(str(t.val))
                stack.append(t.right)
                stack.append(t.left)
 
        return ",".join(l)
 
    # Decodes your encoded data to tree.
    def deserialize(self, data):
        if not data:
            return None
 
        global t
        t = 0
        arr = data.split(",")
        return self.deserialize_helper(arr)
 
    def deserialize_helper(self, arr):
        global t
        if arr[t] == "#":
            return None
 
        # Create node with this item
        # and recur for children
        root = TreeNode(int(arr[t]))
        t += 1
        root.left = self.deserialize_helper(arr)
        t += 1
        root.right = self.deserialize_helper(arr)
        return root
    
    def preorder(self, node):
        if node:
            print(f"{node.val} ")
            self.preorder(node.left)
            self.preorder(node.right)
        
    def flatten(self, root: Optional[TreeNode]) -> None:
    #     from collections import deque
    #     head = temp = root
    #     q = deque()
    #     q.append(root)
    #     while q:
    #         node = q.popleft()
    #         # print(node.val)
    #         if node.left:
    #             q.append(node.left)
    #         if node.right:
    #             q.append(node.right)
    #         if temp != node:
    #             temp.right = node 
    #             temp = temp.right
    #         temp.left = None
    #     return head
    
    # def dfs_and_print_tree_preorder(self, root):
        stack = [root]
        head = temp = root
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
            if temp != node:
                temp.right = node 
                temp = temp.right
            temp.left = None
        return head

            




    
if __name__=='__main__':
    solution = Solution()

    t3 = Node(3)
    t4 = Node(4)
    t2 = Node(2, t3 , t4)

    t6 = Node(6)
    t5 = Node(5, None, t6)
  
    t1 = Node(1, t2 , t5)
    solution.preorder(t1)
    flatten = solution.flatten(t1)
    solution.preorder(t1)

    t0 = Node(0)
    t2 = Node(2)
    t1 = Node(1, t0 , t2)

    t4 = Node(4)
    t6 = Node(6)
    t5 = Node(5, t4, t6)

    t3 = Node(3, t1, t5)
    serialized = solution.serialize(t3) # == '3,1,0,#,#,2,#,#,5,4,#,#,6,#,#'
    print("Serialized view of the tree:")
    print(serialized)
    t = solution.deserialize(serialized)
    inOrder(t)

    t1 = Node(1)
    t2 = Node(2)
    t3 = Node(3)
    t4 = Node(4)
    t5 = Node(5)
    t6 = Node(6)
    t1.left = t2
    t1.right = t5
    t2.left = t3
    t2.right = t4
    t5.right = t6
    height = solution.tree_heightrecursive(t1)
    result = solution.connect(t1)


    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t1.left = t2
    t1.right = t5
    t2.left = t3
    t2.right = t4
    t5.right = t6
    solution.flatten_pre_order_to_linked_list_as_left_will_be_null(t1)



    
    node9 = TreeNode(9)
    node20 = TreeNode(20)
    
    root = TreeNode(3, node9, node20)
    r = solution.levelOrder(root)
    
    
    
    
    
    s = solution.firstBadVersion(5)
    i =0
    
    
    
    
    # nums1 = [2,0]
    # nums2 =[1]
    # solution.merge(nums1, 1, nums2, 1)
    # s = solution.sortedArrayToBST([-10,-3,0,5,9])
    # s = solution.sortedArrayToBST([-3,0,5])
    i
    
    
    # tl4 = TreeNode(1)
    # tl3 = TreeNode(3)
    # tl2 = TreeNode(2, tl3, tl4)
    
    # tr4 = TreeNode(8)
    # tr3 = TreeNode(6)
    # tr2 = TreeNode(7, tr4, tr3)
    # print(solution.levelOrder(TreeNode(5, tr2, tl2)))
    
    # tl4 = TreeNode(4)
    # tl3 = TreeNode(3)
    # tl2 = TreeNode(3, tl3, tl4)
    
    # tr4 = TreeNode(4)
    # tr3 = TreeNode(3)
    # tr2 = TreeNode(3, tr4, tr3)
    
    # t1 = TreeNode(1, tr2, tl2)
    # solution.isSymmetric(t1)
    
    
        
        
        