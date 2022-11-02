class Solution:
    
    def isAdjacentMutant(self, word1, word2)->bool:
        if word2=="#": return False
        cnt=0
        for i, s in enumerate(word1):
            if s!=word2[i]:
                cnt+=1
        return cnt==1
    
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank: return -1
        
        q = collections.deque()
        q.append((start, 0))
        
        while q:
            node, mutation = q.popleft()
            # if got end, Exit
            if node==end: return mutation
            # iterate through bank for next mutant
            for i in range(len(bank)):
                # if adjacent, add to queue, mark it as visited
                if self.isAdjacentMutant(node, bank[i]):
                    q.append((bank[i], mutation+1))
                    bank[i]="#"
        return -1