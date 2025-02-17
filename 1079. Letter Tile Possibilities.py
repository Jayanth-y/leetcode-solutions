class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Step 1: Counting how many times each tile appears
        cc = {} # character-count
        for x in tiles: 
            cc[x] = cc.get(x, 0) + 1  # cc will store the frequency of each character
        
        # Step 2: Set to store unique possibilities
        up = set()

        # Step 3: Define a helper function to build sequences
        def helper(t):
            # Step 3a: If the sequence is not empty, add it to the set
            if t:
                up.add(t)
            
            # Step 3b: Try adding each letter to the sequence
            for x in cc:
                if cc[x] > 0:  # If there are still tiles left of letter 'x'
                    cc[x] -= 1  # Use one letter 'x' (decrease its count)
                    helper(t+x)  # Add 'x' to the current sequence and recurse
                    cc[x] += 1  # Backtrack (put 'x' back for other possibilities)

        # Step 4: Start the recursion with an empty sequence
        helper("")
        
        # Step 5: Return the number of unique sequences (size of the set)
        return len(up)

"""
Leetcode 1079: Letter Tile Possibilities

You have n  tiles, where each tile has one letter tiles[i] printed on it.
Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

Example 1:
Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:
Input: tiles = "AAABBC"
Output: 188

Example 3:
Input: tiles = "V"
Output: 1

Constraints:
1 <= tiles.length <= 7
tiles consists of uppercase English letters.

Approach:
We will use backtracking to explore all possible sequences:
1. Start with an empty sequence.
2. Try to add each tile to the sequence one by one.
3. After adding a tile, recurse and try adding more tiles.
4. We stop when no more tiles are available to add.
5. To avoid counting duplicate sequences, we will store all the sequences in a set (because sets automatically handle duplicates).
"""
