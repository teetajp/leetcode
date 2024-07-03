class Trie:
    def __init__(self, isWord = False):
        self.isWord = isWord
        self.children = {} # lowercase only (26 chars)
    
class WordDictionary:

    def __init__(self):
        self.root = Trie()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            # traverse down trie while creating nodes as necessary
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        
        cur.isWord = True # assuming we are not at root
    
    def search(self, word: str) -> bool:
        n = len(word)
        
        @lru_cache
        def searchRec(cur: Optional[Trie], idx: int) -> bool:
            if idx == n:
                return cur.isWord
            
            nextChar = word[idx] # character we are trying to traverse into
            
            if nextChar == '.':
                return any(searchRec(child, idx + 1) for child in cur.children.values())
            elif nextChar in cur.children:
                return searchRec(cur.children[nextChar], idx + 1)
            else:
                return False
    
        return searchRec(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)