class Node():
    def __init__(self, isWord = False):
        self.isWord = False
        self.children = {}

class Trie():
    def __init__(self):
        self.root = Node()
        
    def add(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        
        cur.isWord = True
                    
        
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        
        while words:
            word = words.pop()
            trie.add(word)
        
        res = []
        
        def findWordsRec(prefix: List[str], cur: Node, row: int, col: int) -> None:
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]) or not cur or len(prefix) >= 10 or board[row][col] not in cur.children:
                return

            ltr = board[row][col]
            prefix.append(ltr)
            board[row][col] = '.' # mark as visited

            cur = cur.children[ltr]
            if cur.isWord: 
                res.append("".join(prefix)) # found new word
                cur.isWord = False # to prevent adding the same word again

            for dr, dc in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                findWordsRec(prefix, cur, row + dr, col + dc)

            prefix.pop() # backtrack
            board[row][col] = ltr # unmark
        
        for ROW in range(len(board)):
            for COL in range(len(board[ROW])):
                findWordsRec([], trie.root, ROW, COL)
        
        return res