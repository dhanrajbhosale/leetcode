class TrieNode:
    def __init__(self):
        self.children = {}
        self.EndOfWord = False
        
    def add_word(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur = cur.children[c]
        cur.EndOfWord = True

class Solution:
    def __init__(self):
        self.num_of_words = 0
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.num_of_words = len(words)
        root = TrieNode()
        for word in words:
            root.add_word(word)  
        res, visit = [], set()

        def dfs(x, y, word, node):
            if x<0 or y<0 or x>=len(board) or y>=len(board[0]) or board[x][y] not in node.children or (x,y) in visit or self.num_of_words == 0:
                return
            visit.add((x,y))
            
            node = node.children[board[x][y]]
            word+=board[x][y]
            if node.EndOfWord:
                res.append(word)
                node.EndOfWord = False
                self.num_of_words-=1
            
            dfs(x+1, y, word, node)
            dfs(x, y+1, word, node)
            dfs(x-1, y, word, node)
            dfs(x, y-1, word, node)

            visit.remove((x,y))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, "", root)

        return res
        