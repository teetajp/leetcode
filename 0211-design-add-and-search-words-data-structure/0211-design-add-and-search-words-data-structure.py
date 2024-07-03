class Trie:
    def __init__(self, letter = None, isWord = False):
        self.letter = letter
        self.isWord = isWord
        self.children = {} # lowercase only (26 chars)

    def __str__(self):
        return f"""Node: ({self.letter}, {self.isWord}, {self.children})"""
    
class WordDictionary:

    def __init__(self):
        self.root = Trie()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            # traverse down trie while creating nodes as necessary
            if c not in cur.children:
                cur.children[c] = Trie(c)
            cur = cur.children[c]
        
        cur.isWord = True # assuming we are not at root

    def search(self, word: str) -> bool:
        n = len(word)

        def searchRec(cur: Optional[Trie], idx: int) -> bool:
            # print(f"search: {cur}, {idx}, {word[idx]}")
            if idx == n:
                return cur.isWord
            
            nextChar = word[idx] # character we are trying to traverse into
            
            if nextChar == '.':
                return any(searchRec(child, idx + 1) for child in cur.children.values())
            elif nextChar in cur.children:
                return searchRec(cur.children[nextChar], idx + 1)
            else:
                return False
                
#             if idx == n-1:
#                 return cur.isWord
#             # if nextChar == '.': # wildcard
#             #     ... ensure at least one word exists
#             #     return any(searchRec(child, idx + 1) for child in cur.children.values())
            
# #             if idx == n-1:
# #                 return (word[idx] == '.') or cur.isWord
# #             elif 
#             else:
                
    
        return searchRec(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)