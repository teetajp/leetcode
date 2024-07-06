class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        BFS to find shortest length path
        
        # Let n be number of words in wordList.
        # Let m be the length of each word (all are the same).
        
        Time Complexity:
            Convert wordList to a set -> O(n)
            We visit a maximum of n words since we avoid previously visited words. -> O(n)
            
            For each word, we try to transition to another word by changing each position to each of the 26 letters of the alphabet and checking if it forms a word in the wordList.
            -> O(n * m * 26) = O(nm)
            
            Even though we could try to transition to each word in the wordList from current word, because we remove visited words from the `wordList`, in total, we only visit O(n) words.
            
            So total time complexity is O(nm), and space complexity is O(n)
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