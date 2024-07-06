class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        BFS to find shortest length path
        """
        wordList = set(wordList) # use it as a list of unexplored words
        queue = collections.deque([beginWord])
        iterCount = 0
        ASCII_a = ord('a')
        
        while queue:
            elemsInLevel = len(queue)
            iterCount += 1
            
            while elemsInLevel > 0:
                word = queue.popleft()
                elemsInLevel -= 1

                if word == endWord:
                    return iterCount

                # try changing each character in the word
                for i in range(len(word)):
                    for ASCII_offset in range(0, 26):
                        nextWord = word[:i] + chr(ASCII_a + ASCII_offset) + word[i+1:]
                        
                        if nextWord in wordList:
                            wordList.remove(nextWord)
                            queue.append(nextWord)
            
        return 0