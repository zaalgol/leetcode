class Solution:
    
    # return all cobinations as sub-arrays of ans, where sum of every combination is the target. 
    # *can use the same number in a combination twice (even its appeatrs only once in the candidates), 
    # but every combenation needs to be different form other combenations - not only in order
    # ([2,2,3] is the same combination of [2,3,2])*
    # All candidates numbers are unique
    def combinationSum(self, candidates, target):
        end = len(candidates)
        def backtrack(tmp, start, target):
            if target == 0:
                ans.append(tmp[:])
            elif target > 0:
                for i in range(start, end):
                    # if i > start and candidates[i] == candidates[i-1]: # we can use it if the candidates are not unique, and we want to avoid duplication of the same sub-array
                    #     continue
                    tmp.append(candidates[i])
                    backtrack(tmp, i, target - candidates[i])
                    tmp.pop()
        ans = [] 
        candidates.sort(reverse= True)
        backtrack([], 0, target)
        # print(ans)
        return ans
    
     # return all cobinations as sub-arrays of ans, where sum of every combination is the target. 
    # *can use the same number in a combination twice only if appeatrs twice in the candidates), 
    # but every combenation needs to be different form other combenations - not only in order
    # ([2,2,3] is the same combination of [2,3,2])*
    # not all candidates numbers are unique.
    def combinationSum2(self, candidates, target):
        def backtrack(start, end, tmp, target):
            if target == 0:
                ans.append(tmp[:])
            elif target > 0:
                for i in range(start, end):
                    if i > start and candidates[i] == candidates[i-1]: # i > start condition will let to use the same number twice, if they are from 2 candidates
                        continue
                    tmp.append(candidates[i])
                    backtrack(i+1, end, tmp, target - candidates[i])
                    tmp.pop()
        ans = []
        candidates.sort(reverse= True)
        backtrack(0, len(candidates), [], target)
        print(ans)
        return ans
    
    # Find subset of nums, all values are quinqe. but as before, no duplicated sub-arrays
    def subsets_iterative(self, nums):
        arr=[[]]
        for n in nums:
            newest =[]
            for a in arr:
               newest.append(a + [n])
            arr += newest
        return arr
    def subsets(self, nums):
        def backtrack(start, end, tmp):
            ans.append(tmp[:])
            for i in range(start, end):
                tmp.append(nums[i])
                backtrack(i+1, end, tmp)
                tmp.pop()
        ans = []
        backtrack(0, len(nums), [])
        return ans
        

    # Find subset of nums, as nums could contain dulication that are could be used in the result. but as before, no duplicated sub-arrays
    def subsetsWithDup(self, nums):
        def backtrack(start, end, tmp):
            ans.append(tmp[:])
            for i in range(start, end):
                if i > start and nums[i] == nums[i-1]:
                    continue
                tmp.append(nums[i])
                backtrack(i+1, end, tmp)
                tmp.pop()
        ans = []
        nums.sort() # sorting for the 'if i > start and nums[i] == nums[i-1]:' check
        backtrack(0, len(nums), [])
        return ans
    
    # array of uniwqe values, retutn permutations
    # example Input: nums = [1,2,3]
    #  Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start, end):
            if start == end:
                ans.append(nums[:])
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1, end)
                nums[start], nums[i] = nums[i], nums[start] # restore the order
                
        ans = []
        backtrack(0, len(nums))
        return ans

    # array of non unique values, retutn permutations, 
    # example Input: nums = [1,1,2]
    #  Output: [[1,1,2],[1,2,1],[2,1,1]]
    def permuteUnique(self, nums):
        def backtrack(tmp, size):
            if len(tmp) == size: # If the length of tmp matches size, this means a complete permutation has been constructed, so it is added to the ans list. The tmp[:]
                ans.append(tmp[:])
            else:
                for i in range(size):
                    # we check 'not visited[i-1]' because if for example we have nums =[1,1,2] and i==0,
                    #  If visited[0] is True, meaning the first 1 is already part of the permutation, the second 1 can be added without causing a duplicate.
                    # If visited[0] is False, meaning the first 1 was skipped, adding the second 1 would create a permutation 
                    # that is a duplicate of one that would have been generated if the first 1 had been used instead.
                    if visited[i] or (i > 0 and nums[i-1] == nums[i] and not visited[i-1]):
                        continue
                    visited[i] = True
                    tmp.append(nums[i])
                    backtrack(tmp, size)
                    tmp.pop()
                    visited[i] = False
        ans = []
        visited = [False] * len(nums)
        nums.sort() # The input list nums is sorted to ensure that duplicates are adjacent.
        backtrack([], len(nums))
        return ans
    
    # example: n = 3, so the permutations are: 1. "123", 2. 132", 3. "213", 4. "231". 5. "312", 6. "321". If k=3, it will retutn the third permutation:"213"
    def getPermutation(self, n, k):
        nums = [str(i) for i in range(1, n+1)] # nums is a sequebce 1,2...n+1. these are the numbers in the permutatios (n+1, not n, because we wont also the last number)
        fact = [1] * n
        for i in range(1,n):
            fact[i] = i*fact[i-1] # will set the value of every item in the array. fact[0]=1, fact[1] =1, fact[2]=2, fact[3] =6...
        k -= 1 # adjust index 1 to python index 0, so it will be k-1
        ans = []
        for i in range(n, 0, -1):
            id = int(k / fact[i-1]) # if for example n=3, k=3, so the third permutation ponits to the second block (because nums[1] = 2)
            k %= fact[i-1] # reducing the problem to find the permutations of the next numbers. (if for example we found the first number '2' for n=3,k=3, 
            # now we only need to find the next number from nums=['1', '3'])
            ans.append(nums[id])
            nums.pop(id)
        return ''.join(ans) # convert to string
    
    # return all partitions, as all partitions sub-strings are palindrome
    # example: Input: s = "aab"
     #    Output: [["a","a","b"],["aa","b"]]
    def partition(self, s):
        def backtrack(start, end, tmp):
            if start == end:
                ans.append(tmp[:])
            for i in range(start, end):
                cur = s[start:i+1]
                if cur == cur[::-1]:
                    tmp.append(cur)
                    backtrack(i+1, end, tmp)
                    tmp.pop()
        ans = []
        backtrack(0, len(s), [])
        return ans
    
    # example: [5,1,4,3,2] -> [5, 2, 1, 3, 4] 
    def next_permutation(self, nums):
        # Find the first element from the right that is not in decreasing order
        i = len(nums) - 2 # -2 and not -1, because we will compare to i+1
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # If such an element is found, find the smallest element from the right that is greater than it
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap the two elements
            nums[i], nums[j] = nums[j], nums[i] # for parameter:[5,1,4,3,2],  -> [5, 2, 4, 3, 1] (because i point on 2 value, and j points on 1 value)
        # Reverse the elements from i+1 to the end to get the next permutation
        nums[i + 1:] = reversed(nums[i + 1:]) # [5, 2, 4, 3, 1] -> [5, 2, 1, 3, 4] 
        print(nums)

    def previous_permutation(self, nums):
        # Find the first element from the right that is not in increasing order
        i = len(nums) - 2  # Start from the second last element
        while i >= 0 and nums[i] <= nums[i + 1]:
            i -= 1

        # If such an element is found, find the largest element from the right that is smaller than it
        if i >= 0:
            j = len(nums) - 1
            while nums[j] >= nums[i]:
                j -= 1
            # Swap the two elements
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the elements from i+1 to the end to get the previous permutation
        nums[i + 1:] = reversed(nums[i + 1:])
        print(nums)
    


solution = Solution()
solution.previous_permutation( [5, 2, 1, 3, 4] )
solution.next_permutation([5,1,4,3,2])
solution.partition("aab")
solution.getPermutation(3,3)
solution.combinationSum2([10,1,2,7,6,1,5],8)
solution.combinationSum([2,3,6,7], 7)

print(solution.combine(4,3))

