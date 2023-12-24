class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # need to encode number of strings, and length of each string
        # first number till the delimiter is the number of strings
        # then, before each string and delimiter, will be the length of each string
        n = len(strs)
        res = []
        res.append(str(n))
        res.append('\r\n')
        
        for w in strs:
            res.append(str(len(w)))
            res.append('\r\n')
            res.append(w)

        return "".join(res)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        delim_idx = s.find('\r\n')
        if delim_idx == -1:
            raise Exception("Invalid message encoding")
            
        num_strs = int(s[:delim_idx])
        
        res = []
        
        i = delim_idx+2
        j = s.find('\r\n', i)

        
        while i < len(s) and j != -1:
            word_len = int(s[i:j])
            word_start = j + 2
            word = s[word_start : word_start+word_len]
            res.append(word)
            
            i = word_start + word_len
            j = s.find('\r\n', word_start)
        
            
            
        return res
        
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))