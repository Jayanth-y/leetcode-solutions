class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cc = {}
        up = set()

        for x in tiles: 
          cc[x] = cc.get(x, 0) + 1

        def helper(t):
            if t: 
                up.add(t)
            
            for x in cc:
                if cc[x] > 0:
                    cc[x] -= 1
                    helper(t+x)                    
                    cc[x] += 1

        helper("")
        return len(up)
