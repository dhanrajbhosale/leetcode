class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a_moves = 0
        b_moves = 0
        
        i=0
        cnt_A = 0
        cnt_B = 0
        for c in colors:
            if c=='A':
                b_moves+=max(cnt_B-2,0)
                cnt_B = 0
                cnt_A+=1
            elif c=='B':
                a_moves+=max(cnt_A-2,0)
                cnt_A = 0
                cnt_B+=1
        a_moves+=max(cnt_A-2,0)
        b_moves+=max(cnt_B-2,0)
        return a_moves>b_moves
