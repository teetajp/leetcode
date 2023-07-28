class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Anagrams are words that have the same character counts
        
        # idea: for each word, get the character frequencies
        # the char freq will be a list or a tuple of 26 letters (alphabet)
        # this tuple will be the key, and value will be the word
        anagrams = dict()
        for word in strs:
            formatted_word = word.lower()
            char_freqs = [0 for i in range(26)] # freq of each alphabet
            for char in word:
                # the Unicode code point for lowercase alphabet is from
                # 97 ('a') to 122 ('z')
                char_freqs[ord(char) - 97] += 1 # increment count
            
            # convert char freqs to tuple to use as key in anagram dict
            freq_key = tuple(char_freqs)
            
            if freq_key not in anagrams:
                anagrams[freq_key] = []    
            anagrams[freq_key].append(word)
        
        result = []
        for anagram_list in anagrams.values():
            result.append(anagram_list)
        
        return result
            