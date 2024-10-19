from typing import List
from heapq import heapify, heappop, heappush

class Solution:
    def k_smallest_pairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Create a priority queue to hold the sum of pairs along with the indices in nums1 and nums2
        # Only consider the first k numbers in nums1 for initial pairing, as we are looking for the k smallest pairs
        priority_queue = [[u + nums2[0], i, 0] for i, u in enumerate(nums1[:k])]
        heapify(priority_queue)  # Convert list into a heap
        
        # for input:[1,2,4,5,6], [3,5,7,9], 3 , the value of priority_queue is [[4, 0, 0], [5, 1, 0], [7, 2, 0]]
        result = []  # Initialize a list to hold the result pairs

        # Iterate until the priority queue is empty or we have found k pairs
        while priority_queue and k > 0:
            # Pop the smallest sum pair from the heap
            sum_pair, index1, index2 = heappop(priority_queue)
          
            # Append the corresponding values from nums1 and nums2 to the result
            result.append([nums1[index1], nums2[index2]])
          
            k -= 1  # Decrement k as we have found one of the k smallest pairs
          
            # If there are more elements in nums2 to pair with the current nums1 element, push the next pair onto the heap
            # we only need to increase index2, because priority_queue already contains all the first k inex1
            if index2 + 1 < len(nums2):
                heappush(priority_queue, [nums1[index1] + nums2[index2 + 1], index1, index2 + 1])

        return result  # Return the list of k smallest pairs
    
solution = Solution()
solution.k_smallest_pairs([1,2,4,5,6], [3,5,7,9], 3)