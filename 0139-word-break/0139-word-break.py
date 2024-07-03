class Trie:
    def __init__(self, isWord = False):
        self.isWord = isWord
        self.children = [None] * 26
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Idea: combine tries and DP?
        
        Can break off into a new word if current window is a word of at least length 1
        
        If no prefix starting at index 0 form a word, return False
        
        [prefix][word] OR [prefix][suffix]
        
        Need to memoize suffix (DP starting at index i)
        
        
        if this fails, 0 | 1 | suffix
        then we can ignore checking this suffix (0 1 | suffix) and check window of next length (0 1 2 | suffix)
        
        DFS on tree (DAG) instead of array DP to save space
        
        Each dict word is at most 20 char; reduces window length.
        """
        # wordDict = set(wordDict)
        ASCII_a = ord('a')
        
        # build Trie with all dictionary words
        
        # TODO: incorporate max/min word length to exit early?
        root = Trie()
        for word in wordDict:
            cur = root
            
            for c in word:
                idx = ord(c) - ASCII_a
                
                if not cur.children[idx]:
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
                return DFS(i+1, cur.children[ord(s[i]) - ASCII_a])
        
        return DFS(0, root)