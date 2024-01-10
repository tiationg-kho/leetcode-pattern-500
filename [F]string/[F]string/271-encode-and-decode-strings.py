class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        def int_to_string(val):
            byte_array = [(val >> (8 * i)) & 0xFF for i in range(4)][:: - 1]
            char_array = [chr(byte) for byte in byte_array]
            string = ''.join(char_array)
            return string
        
        res = ''
        for s in strs:
            res += int_to_string(len(s)) + s
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        def string_to_int(string):
            val = 0
            for i, c in enumerate(string):
                val += ord(c) << (8 * (4 - 1 - i))
            return val

        res = []
        i = 0
        while i < len(s):
            chunk_len = string_to_int(s[i: i + 4])
            i += 4
            res.append(s[i: i + chunk_len])
            i += chunk_len
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

# time O(n)
# space O(1), not counting output
# using string and chunk and bit manipulation