class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        leni = len(board)
        lenj = len(board[0])
        lenw = len(word)
        def exist_helper(i,j,ci):
            if i < 0 or j < 0 or i == leni or j== lenj or board[i][j] != word[ci]:
                return False
            if ci +1 == lenw:
                return True
            else:
                t = board[i][j]
                board[i][j] ='*'
                isExist = exist_helper(i+1,j,ci+1) or exist_helper(i,j+1,ci+1)  \
                    or exist_helper(i-1,j,ci+1) or exist_helper(i,j-1,ci+1)
                board[i][j] = t
                return isExist 
        for i in range(leni):
            for j in range(lenj):
                if exist_helper(i,j,0):
                    return True
        return False       

solution = Solution()
solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")