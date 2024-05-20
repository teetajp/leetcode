class Node:
    def __init__(self, isWordSuffix = False):
        # map or array with 26 boolean vals; use map to save space
        self.children = defaultdict(Node)
        self.isWordSuffix = isWordSuffix
        
class Trie:

    def __init__(self):
        # each level stores array of the alphabet (26 chars), all lowercase
        self.root = Node(isWordSuffix=False)
        

    def insert(self, word: str) -> None:
        # create nodes while traversing path
        idx = 0
        cur = self.root
        while idx < len(word):
            cur = cur.children[word[idx]]
            idx += 1

        cur.isWordSuffix = True

    def search(self, word: str) -> bool:
        idx = 0
        cur = self.root
        while idx < len(word):
            if word[idx] in cur.children:
                cur = cur.children[word[idx]]
                idx += 1
            else:
                return False
        return cur.isWordSuffix
        

    def startsWith(self, prefix: str) -> bool:
        # check if current node is a word or prefix of some word
        idx = 0
        cur = self.root
        while idx < len(prefix):
            if prefix[idx] in cur.children:
                cur = cur.children[prefix[idx]]
                idx += 1
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)