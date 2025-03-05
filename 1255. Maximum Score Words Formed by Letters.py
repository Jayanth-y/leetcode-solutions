class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        # Step 1: Compute the score of each word based on the given letter scores
        def getWordScore(word):
            return sum(score[ord(char) - ord('a')] for char in word)

        # Step 2: Backtracking function to explore all valid word sets
        def backtrack(index, avl_chars):
            # Base case: If we have checked all words, return 0
            if index == len(words):
                return 0
            
            # Step 3: Option 1 - Skip the current word
            max_score = backtrack(index+1, avl_chars)
            word = words[index]
            valid = True  # Check if we can form the word
            
            # Step 4: Check if the word can be formed with available letters
            for char, count in word_freq[index].items():
                if avl_chars[char] < count:
                    valid = False
                    break
            
            # Step 5: Option 2 - Use the current word if valid
            if valid:
                # Reduce available letter counts
                for char, count in word_freq[index].items():
                    avl_chars[char] -= count
                
                # Recur for the next word and include current word's score
                max_score = max(max_score, word_scores[index] + backtrack(index+1, avl_chars))
                
                # Backtrack to restore the letter counts
                for char, count in word_freq[index].items():
                    avl_chars[char] += count
            
            return max_score

        # Step 6: Precompute required data structures
        char_freq = Counter(letters)  # Available letter frequencies
        word_freq = [Counter(word) for word in words]  # Letter frequencies per word
        word_scores = [getWordScore(word) for word in words]  # Precompute word scores

        # Step 7: Start backtracking to find the maximum score
        return backtrack(0, char_freq)
"""
Leetcode 1255: Maximum Score Words Formed by Letters (https://leetcode.com/problems/maximum-score-words-formed-by-letters/description/)

Given a list of words, list of  single letters (might be repeating) and score of every character.
Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).
It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

Example 1:
Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
Output: 23
Explanation:
Score  a=1, c=9, d=5, g=3, o=2
Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
Words "dad" and "dog" only get a score of 21.

Example 2:
Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
Output: 27
Explanation:
Score  a=4, b=4, c=4, x=5, z=10
Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with a score of 27.
Word "xxxz" only get a score of 25.

Example 3:
Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
Output: 0
Explanation:
Letter "e" can only be used once.
 
Constraints:
1 <= words.length <= 14
1 <= words[i].length <= 15
1 <= letters.length <= 100
letters[i].length == 1
score.length == 26
0 <= score[i] <= 10
words[i], letters[i] contains only lower case English letters.

Approach:
1. Precompute Word Scores
  -> Define a helper function getWordScore(word) that computes the score of each word using the score array.
  -> Store the score for each word in a list word_scores.
2. Precompute Letter Frequencies
  -> Use Counter to create char_freq, which tracks the frequency of available letters.
  -> Create word_freq to store the frequency of letters in each word.
3. Use Backtracking to Explore All Possible Word Combinations
  -> Define a recursive function backtrack(index, avl_chars).
  -> Base Case: If we reach the end of the words list, return 0.
  -> Choice 1: Skip the current word and move to the next (backtrack(index + 1, avl_chars)).
  -> Choice 2: Try using the current word if enough letters are available:
    --> Check if the word can be formed using avl_chars.
    --> If valid, update avl_chars by reducing the used letters.
    --> Compute max_score as the sum of the current word score and the recursive call for remaining words.
    --> Restore avl_chars after recursion (backtracking).
  -> Return the maximum score among valid choices.
4. Call the Backtracking Function
5. Start with index 0 and char_freq to find the maximum possible score.
"""
