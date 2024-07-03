class Trie:
    def __init__(self, isWord = False):
        self.isWord = isWord
        self.children = {}
        # self.children = [None] * 26
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Idea: combine tries and DP?

        DFS on tree (DAG) instead of array DP to save space
        
        Each dict word is at most 20 char; reduces window length.
        
        TODO: incorporate max/min word length to exit early?
        """
        ASCII_a = ord('a')
        
        root = Trie()
        while wordDict:
            word = wordDict.pop()

            cur = root
            
            for c in word:
                idx = ord(c) - ASCII_a
                
                if idx not in cur.children:
                    cur.children[idx] = Trie()
                cur = cur.children[idx]
                
            cur.isWord = True
                    
        # traverse
        n = len(s)
        
        @lru_cache
        def DFS(i, cur):
            if not cur:
                return False
            elif i == n: # reached end of whole string
                # last char of string must form a valid word in path
                return cur.isWord
            elif cur.isWord and DFS(i, root):
                # if current path forms a word, try separating it and forming a new word
                return True
            else:
                # otherwise, try extending the current path to see if it forms a word
                idx = ord(s[i]) - ASCII_a
                return idx in cur.children and DFS(i+1, cur.children[idx])
        
        return DFS(0, root)