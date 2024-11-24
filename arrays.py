import collections
from math import log10
import math
from queue import Queue
from collections import deque
from typing import Optional
from collections import Counter

import numpy as np
visit =0
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution(object):
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = {}
        for index, item in enumerate(nums):
            if item in s:
                s[item].append(index)
            else:
                s[item] = [index]
        for i in nums:
            if target - i in s:
                if s[i] != s[target - i]:
                    return [s[i][0], s[target - i ][0]]
                elif len(s[i])>1:
                    return[s[i][0], s[i][1]]
            
            
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenn = len(nums)
        j=0
        previus =-200
        for i in range(lenn):
            if nums[i] != previus:
                previus=nums[j]=nums[i]
                j+=1
        return j
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        temp1 = l1
        temp2 = l2
        l3 = ListNode()
        temp3 = l3
        carry = 0
        
        
        while temp1 or temp2:
            if temp1:
                temp3.val += temp1.val
                temp1= temp1.next
            if temp2:
                temp3.val += temp2.val
                temp2= temp2.next
            temp3.val += carry
            if temp3.val> 9:
                temp3.val -= 10
                carry = 1
            else:
                carry = 0
            if temp1 or temp2 or carry >0:
                temp3.next = ListNode()
                temp3= temp3.next
        if  carry >0:
            temp3.val += carry
        return l3
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lens = len(s)
        if lens <=1:
            return lens
        
        lengthOfLongest=1
        d = {s[0]: 0}
        
        for i in range(1,lens):
            previusIndex = d.get(s[i], None)
            if previusIndex:
                ls = len(d)
                for j in range( i -ls, previusIndex):
                    del d[s[j]]
                lengthOfLongest = max(lengthOfLongest, ls)
            d[s[i]]= i
        return max(lengthOfLongest, len(d))
    
    def maxProfit(self, prices):
        profit = 0
        position = False
        lenpm = len(prices)-1
        for i in range(lenpm):
            if position:
                if prices[i] > prices[i+1]:
                    position = False
                    profit += prices[i]
            else:
                if prices[i] < prices[i+1]:
                    position = True
                    profit -= prices[i]
        if position:
            profit += prices[lenpm]
        return profit
    
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        km = k % len(nums)
        if km == 0:
            return
        nums[:]=nums[-km:]+nums[:-km]
        
        # for i in range(km):
        #     num = nums.pop()
        #     nums.insert(0, num)
        
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # s = set()
        # for n in nums:
        #     if n in s:
        #         return True
        #     s.add(n)
        # return False
    
        # simple and runs a little faster, but using more memory
        s = set(nums)
        if len(s) < len(nums):
                return True
        return False
    
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        len2 = len(nums2)
        if len2 == 0 or len(nums1) == 0:
            return []
        
        output = []
        nums1.sort()
        nums2.sort()
        j=0
        for num1 in nums1:
            while j<len2 and nums2[j]< num1:
                j+=1
            if j==len2:
                break
            if num1==nums2[j]:
                output.append(num1)
                j+=1
        return output
    
    def plusOne(self, digits):
            """
            :type digits: List[int]
            :rtype: List[int]
            """
            carry = 0
            digits[-1] += 1
            for i in range(len(digits)-1, -1, -1):
                digits[i] += carry
                if digits[i] < 10:
                    return digits
                carry = 1
                digits[i] -= 10
            if carry == 1:
                digits = [1] + digits
            return digits
    
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count =0
        lenn = len(nums)
        for i in range(lenn):
            if count >=lenn:
                return
            while nums[i] == 0 and count <lenn:
                count += 1
                nums.append(nums.pop(i))
            count +=1
            
    def isValidSudoku2(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            s = set()
            for cell in row:
                if cell !='.':
                    if cell in s:
                        return False
                    s.add(cell)
                    
        for i in range(9):
            s = set()
            for j in range(9):
                cell = board[j][i]
                if cell !='.':
                    if cell in s:
                        return False
                    s.add(cell)
                    
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                s = set()
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        cell = board[x][y]
                        if cell !='.':
                            if cell in s:
                                return False
                            s.add(cell)
                                
        return True
    
    def isPalindrome(self, s: str) -> bool:
        lens = len(s)
        ss = 0
        tt = lens-1
        while ss < tt:
            if not s[ss].isalpha():
                ss +=1
            if not s[tt].isalpha():
                tt -=1
            if ss >= tt:
                return True
            if s[ss].lower() != s[tt].lower():
                return False
            ss +=1
            tt -=1
        return True
    
    def removeElement(self, nums: list[int], val: int) -> int:
        lenn = len(nums)
        end = lenn-1
        i=0
        for i in range(lenn):
            if (nums[i] == val):
                while end > -1 and nums[end] == val:
                    end -=1
                if (end <= i):
                    return i
                temp = nums[i]
                nums[i] = nums[end]
                nums[end] = temp
        return i+1
    
    # def jump(self, nums: list[int]) -> bool:
    #     steps = [1] * len(nums)
    #     result =  self.canJump_helper(nums, 0, steps)
    #     return result

    # def jump_helper(self, nums: list[int], index, steps) -> bool: 
    #     global  visit
    #     visit +=1
    #     print(visit)
    #     if index ==  len(nums) -1 or steps[index] == 2:
    #         return True
    #     if index >=  len(nums) or nums[index] == 0 or steps[index] == 0:
    #         return False
    #     for i in range(1, min(nums[index] +1, len(nums) + 1)):
    #         if self.canJump_helper(nums, index +i, steps):
    #             steps[index] = 2
    #             return True
    #     steps[index] == 0
    #     return False
    
    def jump(self, nums: list[int]) -> int:
        lenn = len(nums)
        if lenn == 1:
            return 0
        steps = [lenn] * lenn
        result =   self.jump_helper(nums, 0, steps, lenn)
        return result

    def jump_helper(self, nums, index, steps, lenn) -> int: 
        global  visit
        visit +=1
        # print(visit)
        if index ==  lenn -1:
            steps[index] =0
            return 0
        if  steps[index] != lenn:
            return steps[index]
        for i in range(index +1, min(nums[index] +index+1, lenn)):
            steps[index] = min(steps[index], self.jump_helper(nums, i, steps, lenn))
        steps[index] += 1
        return steps[index]
    
    def candy_old(self, ratings: list[int]) -> int:
        lenr = len(ratings) 
        candies= [1]* lenr
        first_changed = 1
        last_changed = lenr - 1
        while(first_changed != lenr):
            s = first_changed - 1
            e = last_changed + 1
            first_changed = lenr
            last_changed = -1
            for i in range (s, e):

                if (i < 0 or i >= lenr ):
                    continue
                if  i !=lenr-1:
                     if ratings[i] > ratings[i +1] and candies[i] <= candies[i +1]:
                        first_changed = min(first_changed, i)
                        last_changed = max(last_changed, i)
                        candies[i] = candies[i +1] +1
                if  i !=0:
                    if ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
                        first_changed = min(first_changed, i)
                        last_changed = max(last_changed, i)
                        candies[i] = candies[i -1] +1

        return sum(candies)

        
    def candy_old_2(self, ratings: list[int]) -> int:
        lenr = len(ratings) 
        candies= [1]* lenr
        q = Queue(maxsize = lenr)
        try:
            for i in range (0, lenr):
                if  i !=lenr-1 and ratings[i] > ratings[i +1] and candies[i] <= candies[i +1]:
                    candies[i] = candies[i +1] +1
                    q.put(i-1)
                if  i !=0 and ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
                    candies[i] = candies[i -1] +1
                    q.put(i+1)
        except Exception as e:
            print(e)
        j=0
        while not q.empty():
            i= q.get()
            if  i !=lenr-1 and ratings[i] > ratings[i +1] and candies[i] <= candies[i +1]:
                candies[i] = candies[i +1] +1
                q.put(i-1)
            if i !=0 and ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
                candies[i] = candies[i -1] +1
                q.put(i+1)

        return sum(candies)
    
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)

        answer = 0
        left = [1] * n
        right = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1

        for a, b in zip(left, right):
            answer += max(a, b)

        return answer

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j].isdigit():
                    if board[i][j] in s:
                        return False
                    s.add(board[i][j])
        for i in range(9):
            s = set()
            for j in range(9):
                if board[j][i].isdigit():
                    if board[j][i] in s:
                        return False
                    s.add(board[j][i])
        li =[[0,0], [0,3], [0,6],  [3,0], [6,0],  [3,3], [6,3], [3,6], [6,6]]
        for l in li:
            i=l[0]
            j=l[1]
            s = set()
            for i in range(l[0], l[0] +3):
                for j in range(l[1], l[1] +3):
                    if board[i][j].isdigit():
                        if board[i][j] in s:
                            return False
                        s.add(board[i][j])
        return True
    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i in range(len(nums)):
            if target -nums[i] in d:
                return [i, d[target -nums[i]]]
            d[nums[i]]=i
            
    def rotate(self, matrix: list[list[int]]) -> None:
        matrix[:] = np.array(matrix[::-1]).T.tolist() # using numpy
        
        
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        leny = len(board) - 1
        lenx = len(board[0]) -1
        new_board = [row[:] for row in board]
        for y in range(leny +1):
            for x in range(lenx+1):
                s =0
                if y > 0 and x > 0 and board[y-1][x-1]:
                    s += 1
                if y < leny and x < lenx and board[y+1][x+1]:
                    s += 1
                if y < leny and x > 0 and board[y+1][x-1]:
                    s += 1
                if y > 0 and x < lenx and  board[y-1][x+1]:
                    s += 1
                if y > 0 and board[y-1][x]:
                    s += 1
                if x > 0 and board[y][x-1]:
                    s += 1
                if y < leny and board[y+1][x]:
                    s += 1
                if x < lenx and board[y][x +1]:
                    s += 1


                if board[y][x] and s < 2 or s > 3:
                        new_board[y][x] = 0
                elif not board[y][x] and s == 3:
                    new_board[y][x] = 1
                # else:
                #     new_board[y][x] = board[y][x]
        
        board[:] = new_board 
      
      
    # ??
    def simplifyPath(self, path: str) -> str:
        stack = []

        for str in path.split('/'):
            if str in ('', '.'):
                continue
            if str == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(str)

        return '/' + '/'.join(stack)
   
    # ??
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        op = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b),
        }

        for token in tokens:
            if token in op:
                b = stack.pop()
                a = stack.pop()
                stack.append(op[token](a, b))
            else:
                stack.append(int(token))

        return stack.pop()
    
    # def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
    #     lenn = len(gas)
    #     low_index = -1
    #     low_value = 20000
    #     curr_val = 0
    #     for i in range(lenn):
    #         curr_val += gas[i] - cost[i]
    #         if curr_val <= low_value:
    #             low_value = curr_val
    #             low_index = i

    #     j = 0
    #     i = low_index + 1
    #     gap = 0
    #     while (j < lenn):
    #         i = i if i < lenn else 0
    #         gap +=gas[i] - cost[i]
    #         if gap < 0:
    #             return -1
    #         j += 1
    #     return low_index + 1
    
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        lenn = len(gas)
        low_index = -1
        low_value = 20000
        curr_val = 0
        for i in range(lenn):
            curr_val += gas[i] - cost[i]
            if curr_val <= low_value:
                low_value = curr_val
                low_index = i

        j = 0
        i = low_index + 1 if low_index < lenn-1 else 0
        gap = 0
        while (j < lenn):
            # i = i if i < lenn else 0
            gap +=gas[i] - cost[i]
            if gap < 0:
                return -1
            j += 1
            i = i + 1 if i < lenn-1 else 0


        # return low_index + 1
        return i
    
    def searchInsert(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) -1
        while True:
            mid = int((end + start) /2 )
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                if end == mid:
                    return end +1
                start = mid + 1
            else:
                if start == mid:
                    return start
                end = mid -1
                
    def addBinary(self, a: str, b: str) -> str:
        lena = len(a)
        lenb = len(b)
        if lena < lenb:
            t = lena
            lena = lenb
            lenb = t
            t = a
            a = b
            b =t
            
        ap = lena-1
        s = ""
        c = 0
        for bp in range(lenb-1, -1, -1):
            sum = int(a[ap]) + int(b[bp]) + c
            if sum == 0 or sum == 1:
                c = 0
                s += str(sum)
            elif sum == 2:
                c =1
                s += '0'
            else:
                s += '1'
                c =1
            ap -= 1
        for ap in range(ap, -1, -1):
            sum = int(a[ap])+ c
            if sum == 0 or sum == 1:
                s += str(sum)
                c = 0
            elif sum == 2:
                c =1
                s += '0'
            else:
                s += '1'
                c =1
            ap -= 1
        if c == 1:
            s += '1'
            # if s[:-1]  == '0':
            #     s[:-1] = '1'
            # else:
            #     s = s[:-1] +  '01'
        s = s[::-1]
        # if ap >= 0:
        #     s = a[0:ap+1] + s
        return s
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        k = None
        r = None
        if not list2 and list1.val < list2.val:
            k=list1
            i = list1.next
            j = list2
        else:
            k=list1
            i = list1.next
            j = list2
        
        while i:
            if j:
                if i.val < j.val:
                    item = i
                    i = i.next
                else:
                    item = j
                    j = j.next
            else:
                item = i
                i = i.next


        while j:
            item = j
            j = j.next
            k.append(item)
        t = k[0]
        r = t
        t = t.next
        for item in k[1:]:
            t=item
            t = t.next
        return r
            
    def maxProfit3(self, prices: list[int]) -> int:
        profits = []
        current = 0
        lenp =len(prices)
        for i in range(lenp -1):
            if prices[i] > prices[i+1]:
                if current:
                    profits.append(prices[i] - current)
                    current = 0
            elif prices[i] < prices[i+1]:
                if not current:
                    current = prices[i]
        
        if current:
            profits.append(prices[lenp -1] - current)

        return profits.sort(reverse=True)[:2]
    
    def summaryRanges(self, nums: list[int]) -> list[str]:
        output =[]
        start = None
        lenn = len(nums)
        for i in range(lenn):
            if not start:
                start = f"{nums[i]}"
                if i == lenn-1 or nums[i+1] > nums[i] +1:
                    output.append(f"{start}")
                    start = None
            elif i == lenn-1 or nums[i+1] > nums[i] +1:
                    output.append(f"{start}->{nums[i]}")
                    start = None
        return output
    
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        s = []
        intervals = sorted(intervals, key=lambda x: x[0])
        for i in intervals:
            if not s:
                s.append(i)
            else:
                before = s.pop() 
                if before[1] < i[0]:
                    s.append(before)
                    s.append(i)
                else:
                    s.append([before[0],max(before[1], i[1])])
        return s
        
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        dr={}
        t=0
        lens = len(s)
        for c in pattern:
            if  t==lens:
                return False  
            word=''
            while t<lens and  s[t] == ' ':
                t +=1
            while t<lens and s[t] != ' ':
                word += s[t]
                t +=1
            if c in d:
                if word != d[c] or word not in dr or c != dr[word]:
                    return False
            else:
                if word  in dr:
                    return False
                d[c] = word
                dr[word] = c
        if  t<lens:
            return False     
        return True  
    
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        num3 = []
        d = dict(Counter(nums))
        numss = [] 
        for key in d:
            if d[key] >= 3:
                numss.append(key)
                numss.append(key)
                numss.append(key)
            elif d[key] == 2:
                numss.append(key)
                numss.append(key)
            else:
                numss.append(key)
            
        lenn = len(numss)
        for ii in range(lenn):
            i = numss[ii]
            for jj in range (ii+1, lenn):
                j = numss[jj]
                k = - j -i
                if k in d:
                    if (i == j == k and d[k] <3) or ((i==k or j==k) and d[k] <2):
                        continue
                    num3.append(sorted([i,j,k]))

        return np.unique(num3, axis=0).tolist()
    
    
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        arr = [[] for i in range(numRows)]
        for i in range(len(s)):
            modulo = i % (numRows * 2 -2)
            if modulo >= numRows:
                gap = modulo - numRows +1
                modulo = numRows -1 -gap
            arr[modulo].append(s[i])
        res = ""
        for a in arr:
            res +=  "".join(a)
        return res
    
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        while x >=10:
            number_of_digits = int(log10(x))
            most_signficant = x // (10 ** number_of_digits)
            less_significant = x % 10 
            if most_signficant != less_significant:
                return False
            x -= most_signficant * 10 ** number_of_digits
            x = x // 10
            if not x:
                return True
            new_number_of_digits = int(log10(x))
            diff = number_of_digits - new_number_of_digits - 2 
            if diff:
                if x % (10 ** diff):
                    return False
                x = int(x / 10 ** diff)
        return True
    
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        total = 1
        nums_of_zeros = 0
        for i in nums:
            if not i:
                nums_of_zeros +=1
            else:
                total *= i
        if not nums_of_zeros:
            return [total // i for i in nums]
        elif nums_of_zeros ==1:
            result = []
            for i in nums:
                if i == 0:
                    result.append(total)
                else:
                    result.append(0)
            return result
        else:
            return [0] * len(nums)
        
    def isIsomorphic(self, s: str, t: str) -> bool:
        sss = map(s.index, s)
        ttt = map(t.index, t)
        return [*map(s.index, s)] == [*map(t.index, t)]
    
    
    def longestConsecutive(self, nums: list[int]) -> int:
        if not len(nums):
            return 0
        max_l = 1
        s = set(nums)
        for n in s:
            if not n-1 in s:
                max_t = 1
                i=n+1
                while i in s:
                    max_t +=1
                    i +=1
                max_l = max(max_l, max_t)
        return max_l
     
    def intToRoman(self, num: int) -> str:
        s = ''
        if num >=1000:
            thouthends = int(num/1000)
            s += 'M' * thouthends
            num -= thouthends * 1000
        if num >=900:
            num -=900
            s += 'CM'
        if num >=400:
            num -=400
            s += 'CD'
        if num >=100:
            hundreds = int(num/100)
            s += 'C' * hundreds
            num -= hundreds * 100
        if num >=90:
            num -=90
            s += 'XC'
        if num >=40:
            num -=40
            s += 'XL'
        if num >=10:
            tens = int(num/10)
            s += 'X' * tens
            num -= tens * 10
        if num >=9:
            num -=9
            s += 'XC'
        if num >=4:
            num -=4
            s += 'IX'
        s+= 'I' * num
        return s
    
    def entityParser(self, text: str) -> str:
        d = {
            '&quot;': '\"',
            '&apos;': '\'',
            '&amp;': '&',
            '&gt;': '>',
            '&lt;': '<',
            '&frasl;': '/',
        }

        new_s = ""
        i=0
        while i < len(text):
            entity = False
            for k in d.keys():
                if text[i:].startswith(k):
                   new_s += d[k] 
                   i += len(k)
                   entity = True
                   break
            if not entity:
                new_s += text[i]
                i +=1

        return new_s
            
            
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        lena = len(arr)
        sum_a =sum(arr)
        if sum_a% 3:
            return False
        third = sum_a /3
        left_third = 0
        right_third = 0
        for l,v in enumerate(arr):
            left_third += v
            if  left_third == third:
                break
        for r, v in enumerate(reversed(arr)):
            original_index_r = lena - 1 - r
            if l+1 >=original_index_r:
                return False
            right_third += v
            if  right_third == third:
                break
        
        return True
    
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        for y in range(len(obstacleGrid)):
            for x in range(len(obstacleGrid[0])):
                if obstacleGrid[y][x]:
                    obstacleGrid[y][x] =0
                else:
                    obstacleGrid[y][x] =1
        for y in range(len(obstacleGrid)):
            for x in range(len(obstacleGrid[0])):
                if not obstacleGrid[y][x]:
                    continue
                if y > 0 and x > 0:
                    obstacleGrid[y][x] = obstacleGrid[y][x-1] + obstacleGrid[y-1][x] 
                elif y > 0:
                    obstacleGrid[y][x] =  obstacleGrid[y-1][x] 
                elif x > 0:
                    obstacleGrid[y][x] =  obstacleGrid[y][x-1] 
        return obstacleGrid[-1][-1]
    
    
    def subarraySum(self, nums: list[int], k: int) -> int:
        ans = 0
        prefix = 0
        count = collections.Counter({0: 1}) # inint a dict with {0: 1}

        for num in nums:
            prefix += num
            ans += count[prefix - k] # if for example nums = [2,5,8,3,2,3], k=11, so after 2,5, count[7]=1, and when num=3 - prefix=18 and count[prefix - k] = 1
            count[prefix] += 1

        return ans

    def findAnagrams(self, s: str, p: str):
        lens = len(s)
        lenp = len(p)
        ans = []
        while lenp<=lens:
        # if lenp > len(s):
        #     return []
            d = Counter(p)
            prev = ''
            for i, c in enumerate(s):
                if i >=lenp:
                    d[prev]-=1
                    if not d[prev]:
                        del d[prev]
                if c in d:
                    d[c]-=1
                    if not d[c]:
                        del d[c]
                        if d == {}:
                            ans.append(i-lenp+1)
                            break
                else:
                    d[c]=1
                prev = c
            # if i>=lens-lenp:
            #     break
            s=s[i-lenp+2:]
            lens = len(s)
        return ans
    
    # works, but slow
    # def wordBreak(self, s: str, wordDict: list[str]) -> bool:
    #     lens = len(s)
    #     arr = [1] * lens
    #     wordDict.sort(reverse=True)
        
    #     def wordBreak_helper(i):
    #         if i==lens or arr[i]==2:
    #             return True
    #         if arr[i]==0:
    #             return False
    #         for word in wordDict:
    #             if s[i:].startswith(word):
    #                 if wordBreak_helper(i + len(word)):
    #                     arr[i] = 2
    #                     return True
    #         arr[i] = 0
    #         return False
    #     return wordBreak_helper(0)

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        lens = len(s)
        arr = [True] * lens
        wordDict.sort(reverse=True)
        
        def wordBreak_helper(i):
            if i==lens:
                return True
            if not arr[i]:
                return False
            for word in wordDict:
                if s[i:].startswith(word):
                    if wordBreak_helper(i + len(word)):
                        return True
            arr[i] = False
            return False
        return wordBreak_helper(0)
    
    def wordBreak_iterative(self, s: str, wordDict: list[str]) -> bool:
        lens = len(s)
        arr = [False] * lens
        for i in range(lens - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= lens and s[i:i+len(w)] == w:
                    if i + len(w) == lens or arr[i + len(w)]:
                        arr[i] = True
                        break
        return arr[0]

    def minDistance(self, word1: str, word2: str) -> int:
        lenw1=len(word1)
        lenw2=len(word2)
        if not lenw1:
            return lenw2
        if not lenw2:
            return lenw1  

        arr=[[j for j in range(lenw2 + 1)]]
        for i in range(1, lenw1 + 1):
            a = [i]
            for j in range(1, lenw2 + 1):
                a.append(0)
            arr.append(a)

        for i in range(1, lenw1 + 1):
            for j in range(1, lenw2 + 1):
                if word1[i-1] == word2[j-1]:
                    arr[i][j]=arr[i-1][j-1]
                else:
                    arr[i][j] = min(arr[i-1][j-1], arr[i-1][j], arr[i][j-1]) + 1

        return arr[lenw1][lenw2]
    
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        leny = len(matrix)
        lenx = len(matrix[0])
        maxi = 0
        for i in range( leny):
            for j in range(lenx):
                matrix[i][j] = int(matrix[i][j])
        for i in range(1, leny):
            for j in range(1, lenx):
                if matrix[i][j]:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1]) + 1
                    maxi = max(maxi, matrix[i][j])
        return maxi**2
    
    #compose s3 fro s1 and s2 in order
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        # t1 = t2 = t3 = 0
        # for i in range(len3):
        #     if t1 < len1 and s3[i] == s1[t1]:
        #         t1+=1
        #     elif t2 < len2 and s3[i] == s2[t2]:
        #         t2+=1
        #     else:
        #         return False

        boolean_matrix = [[True] * len2 for _ in range(len1)]
        
        def isInterleave_helper(i1, i2, i3) -> bool:
            if i1 < len1 and i2 < len2 and not boolean_matrix[i1][i2]:
                return False
            if i3==len3:
                if i1 == len1 and i2 == len2:
                    return True
                return False
            if i1 == len1:
                return s2[i2:]==s3[i3:]
            if i2 == len2:
                return s1[i1:]==s3[i3:]
            
            if s1[i1] == s3[i3]:
                result = isInterleave_helper(i1+1, i2, i3+1)
                if not result:
                    boolean_matrix[i1][i2]=False
                else:
                    return True
            if s2[i2] == s3[i3]:
                result = isInterleave_helper(i1, i2+1, i3+1)
                if not result:
                    boolean_matrix[i1][i2]=False
                else:
                    return True
            return False
            
        return isInterleave_helper(0,0,0)

    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        mi=len(nums) + 1
        start = 0
        end = 0
        sum=nums[0]
        while True:
            if sum >= target:
                mi = min(mi, end-start+1)
                sum -= nums[start]
                start +=1
                if start == len(nums):
                    break
            else:
                end+=1
                if end == len(nums):
                    break
                sum += nums[end]
        return mi if mi <= len(nums) else 0

    def minSubArrayLen_2(self, s: int, nums: list[int]) -> int:
        ans = math.inf
        summ = 0
        j = 0

        for i, num in enumerate(nums):
            summ += num
            while summ >= s:
                ans = min(ans, i - j + 1)
                summ -= nums[j]
                j += 1

        return ans if ans != math.inf else 0
    
    # binary search in rotate array
    def search(self, nums: list[int], target: int) -> int:
        # start = 0
        # end = len(nums) - 1
        # mid = (end + start) // 2 
        # while end >= start:
        #     if nums[mid] == target:
        #         return mid
        #     if nums[mid] > target:
        #         if nums[mid] > nums[end]:
        #             start = mid +1
        #         else:
        #             end = mid -1
        #     else:
        #         if nums[mid] < nums[start]:
        #             end = mid -1
        #         else:
        #             start = mid +1
        #     mid = (end + start) // 2 
        # return -1
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:  # nums[l..m] are sorted.
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:  # nums[m..n - 1] are sorted.
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1

    
    
    
        
solution = Solution()
solution.search([4,5,6,7,0,1,2], 0)

solution.minSubArrayLen(7, [2,3,1,2,4,3])

solution.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
solution.minDistance("ros", "horse")
solution.minDistance("horse", "ros")

solution.findAnagrams("cbaebabacd", "abc")
solution.subarraySum([2,5,8,3,2,3], 11)
# solution.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
solution.uniquePathsWithObstacles([[1,0]])

solution.canThreePartsEqualSum([14,6,-10,2,18,-7,-4,11])
solution.entityParser("&amp; is an HTML entity but &ambassador; is not.")

solution.intToRoman(3749)
solution.longestConsecutive([100,4,200,1,3,2])

solution.isIsomorphic(s = "paper", t = "title")


r = solution.isPalindrome(11)
r = solution.isPalindrome(10201)
r = solution.isPalindrome(1000021)

solution.convert("PAYPALISHIRING", 1)

r = solution.threeSum([-1,0,1,2,-1,-4])

solution.wordPattern("a","a")
solution.wordPattern("aaaa","aa aa aa")
solution.wordPattern("aaa","aa aa aa aa")
solution.wordPattern("abc","dog cat dog")
solution.wordPattern("abba", "dog dog dog dog")
solution.wordPattern("abba", "dog cat cat dog")
solution.wordPattern("abba", s = "dog cat cat fish")
solution.wordPattern(pattern = "aaaa", s = "dog cat cat dog")


solution.merge([[1,3],[2,6],[8,10],[15,18]])
result = solution.summaryRanges([0,1,2,4,5,7])
results = solution.maxProfit3([3,3,5,0,0,3,1,4])

l4 = ListNode(4)
l3 = ListNode(3, l4)
l1 = ListNode(1, l3)

ll4 = ListNode(4)
ll1 = ListNode(1, ll4)
solution.mergeTwoLists(l1, ll1)
solution.mergeTwoLists()
solution.addBinary("1", "111")
solution.addBinary("1010", "1011")
solution.addBinary("11", "1")
solution.searchInsert([1,3,5,6], 2)
solution.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])   
solution.canCompleteCircuit([2,3,4], [3,4,3])     
solution.canCompleteCircuit([3,1,1], [1,2,2])     
solution.evalRPN(["3","11","5","+","-"])
solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
solution.evalRPN(["2","1","+","3","*"])
solution.simplifyPath("/home//foo/")
board = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,1,1,1,0],[0,1,1,1,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
solution.gameOfLife(board)
solution.twoSum([2,7,11,15], 9)
solution.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
#solution.candy([1,0,2])
# solution.candy([1,2,2])
# solution.candy([1,3,2,2,1])
#solution.candy([1,2,87,87,87,2,1])
# print(solution.jump([2,3,1,1,4]))
# print(solution.jump([2,3,0,1,4]))
# print(solution.jump([1,2,3]))
#print(solution.jump([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,7,3,8,5]))

solution.removeElement([1], 1)

print(solution.isPalindrome("A man, a plan, a canal: Panama"))

# board = [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]

# board = [["8","3",".",".","7",".",".",".","."],
#          ["6",".",".","1","9","5",".",".","."],
#          [".","9","8",".",".",".",".","6","."],
#          ["8",".",".",".","6",".",".",".","3"],
#          ["4",".",".","8",".","3",".",".","1"],
#          ["7",".",".",".","2",".",".",".","6"],
#          [".","6",".",".",".",".","2","8","."],
#          [".",".",".","4","1","9",".",".","5"],
#          [".",".",".",".","8",".",".","7","9"]]


# board = [["5","3",".",".","7",".",".",".","."],
#          ["6",".",".","1","9","5",".",".","."],
#          [".","9","8",".",".",".",".","6","."],
#          ["8",".",".",".","6",".",".",".","3"],
#          ["4",".",".","8",".","3",".",".","1"],
#          ["7",".",".",".","2",".",".",".","6"],
#          [".","6",".",".",".",".","2","8","."],
#          [".",".",".","4","1","9",".",".","5"],
#          [".",".",".",".","8",".",".","7","9"]]
# print(solution.isValidSudoku(board))

# nums = [0]
# solution.moveZeroes(nums)
# print(nums) # [5, 6, 7, 1, 2, 3, 4]

# result = solution.plusOne([9])
# print(result) # [5, 6, 7, 1, 2, 3, 4]


# result = solution.intersect([1,2,2,1],[2])
# print(result) # [5, 6, 7, 1, 2, 3, 4]


# nums = [1,2,3,4,5,6,7]
# solution.rotate(nums, 3)
# print(nums) # [5, 6, 7, 1, 2, 3, 4]

# result = solution.maxProfit([7,6,4,3,1])
# print(result)

# result = solution.lengthOfLongestSubstring('abcab56')
# print(result)

# result = solution.twoSum([3,2,4], 6)
# print(result)

# nums = [2,4,4,5,6,8,8,9]
# result = solution.removeDuplicates(nums)
# print(result)
# print(nums)


 