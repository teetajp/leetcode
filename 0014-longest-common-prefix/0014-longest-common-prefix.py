class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Keep a count of max prefix length and a count of current prefix length, when there is a mismatch, stop.
        str_count, min_str_len = len(strs), min( len(s) for s in strs )
        last_index = 0
        for i in range(min_str_len):
            for j in range(1, str_count):
                if strs[j][i] != strs[j-1][i]:
                    return strs[0][0:last_index]
            last_index += 1
            
        return strs[0][0:last_index]