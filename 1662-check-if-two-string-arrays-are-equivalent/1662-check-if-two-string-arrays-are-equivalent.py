class Solution:    
    # TC O(n) SC O(n)
    # def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # return "".join(word1)=="".join(word2)
    
    # TC O(min(m,n)) => exits when it finds the first mismatch character
    # SC O(1) => comparison on the fly.
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        for c1, c2 in zip(self.generate(word1), self.generate(word2)):
            if c1 != c2:
                return False
        return True

    def generate(self, wordlist: List[str]):
        for word in wordlist:
            for char in word:
                yield char
        yield None
        