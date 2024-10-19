class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result <<= 1        # Shift result left by 1 to make space for the next bit
            result |= (n & 1)   # Add the least significant bit of n to result
            n >>= 1             # Shift n right by 1 to process the next bit
        return result
    

solution = Solution()
