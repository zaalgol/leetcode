class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}

        for a, b in zip(s, s[1:]):
            if roman[a] < roman[b]:
                ans -= roman[a]
            else:
                ans += roman[a]

        return ans + roman[s[-1]]

    def hammingDistance(self, x: int, y: int) -> int:
        count =0
        while x and y:
            cx = x%2
            cy = y%2
            if cx != cy:
                count += 1
            if cx:
                x -=1
            if cy:
                y -=1
            x /=2
            y /=2
            
        m = max(x,y)
            
        while m> 0:
            if m%2:
                count += 1
                m -=1
            m /=2
        return count
    
    def generate(self, numRows: int):
        output = [[1]]
        for i in range (1, numRows):
            line = [1]
            for a, b in zip(output[i-1], output[i-1][1:]):
                line.append(a+b)
            line.append(1)
            output.append(line)
        return output
    
    def isValid(self, s: str) -> bool:
        a = []
        for c in s:
            if c in [')',']','}']:
                if not a:
                    return False
                b = a.pop()
                if (c == ')' and b != '(') or (c == ']' and b != '[') or  (c == '}' and b != '{') :
                    return False
            if c in ['(','[','{']:
                a.append(c)
        if a:
            return False
        return True
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        t1 = t2 = t3 = 0
        for i in range(len3):
            if t1 < len1 and s3[i] == s1[t1]:
                t1+=1
            elif t2 < len2 and s3[i] == s2[t2]:
                t2+=1
            else:
                return False
    
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2 == 1:
            return x * self.myPow(x, n - 1)
        # return self.myPow(x, n//2) * self.myPow(x, n//2)
        return self.myPow(x * x, n // 2)
    
    

s = Solution()
s.isInterleave("aabcc", "dbbca", "aadbbcbcac")

s.isValid('()')
s.generate(5)
s.hammingDistance(1,4)
s.romanToInt("LVII")