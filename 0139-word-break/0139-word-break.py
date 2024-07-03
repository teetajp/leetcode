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
        If i == n:
            return isWord
        If isWord and DFS(i+1, self.root):
            return True
            # break word and continue, or continue word
        return DFS(i+1, cur.children[c])
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
        
        @cache
        def DFS(i, cur):
            # what about not cur?
            # if not cur:
                # return False
            if i == n:
                # reached end of whole string, just need to check whether current path is a valid word
                return cur.isWord
            
            idx = ord(s[i]) - ASCII_a
            # if current path forms a word, try separating it and forming a new word
            # otherwise, try extending the current path to see if it forms a word
            return (cur.isWord and DFS(i, root)) or (cur.children[idx] and DFS(i+1, cur.children[idx]))
        
        return DFS(0, root)