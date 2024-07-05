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
        
    def findWords(self, res: List[str], prefix: List[str], cur: Node, row: int, col: int, board: List[List[str]]) -> None:
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
            self.findWords(res, prefix, cur, row + dr, col + dc, board)
        
        prefix.pop() # backtrack
        board[row][col] = ltr # unmark
            
        
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        
        while words:
            word = words.pop()
            trie.add(word)
        
        res = []
        
        for ROW in range(len(board)):
            for COL in range(len(board[ROW])):
                trie.findWords(res, [], trie.root, ROW, COL, board)
        
        return res