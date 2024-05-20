class keydefaultdict(defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        else:
            ret = self[key] = self.default_factory(key)
            return ret
    # https://stackoverflow.com/questions/31723719/how-to-use-a-specific-data-structure-as-the-default-factory-for-a-defaultdict
    # defaultdict but uses key as argument of the default factory/constructor
class Node:
    def __init__(self, val = "", isWordSuffix = False):
        self.val = val
        # map or array with 26 boolean vals; use map to save space
        self.children = keydefaultdict(Node)
        self.isWordSuffix = isWordSuffix
        
class Trie:

    def __init__(self):
        # each level stores array of the alphabet (26 chars), all lowercase
        self.root = Node(val="", isWordSuffix=False)
        

    def insert(self, word: str) -> None:
        node = self.findNodeCreate(self.root, [word], 0)
        node.isWordSuffix = True

    def search(self, word: str) -> bool:
        node = self.findNodeStop(self.root, [word], 0)
        return node and node.isWordSuffix
        

    def startsWith(self, prefix: str) -> bool:
        node = self.findNodeStop(self.root, [prefix], 0)
        # check if current node is a word or prefix of some word
        return node and (node.isWordSuffix or len(node.children) > 0)
            
    
    def findNodeCreate(self, node: Node, word: list[str], idx: int) -> Node:
        # create nodes while traversing path
        if idx < len(word[0]):
            return self.findNodeCreate(node.children[word[0][idx]], word, idx+1)
        else:
            return node
    
    def findNodeStop(self, node: Node, word: list[str], idx: int) -> Node:
        # search for word, stopping early
        #   if node we're in doesn't have suffix we are looking for
        if idx < len(word[0]) and word[0][idx] in node.children:
            return self.findNodeStop(node.children[word[0][idx]], word, idx+1)
        elif idx == len(word[0]):
            return node
        else:
            return None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)