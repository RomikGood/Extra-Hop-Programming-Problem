import scraping

def find_longest_word(grid, words):


    """
    Recursive function to verify that the candidate word exists in the grid
    and if it does, funcion returns the word's length
    """
    def if_word_exists(grid, word, r, c, index):
        word = word.upper()
        
        # Valid chess knight moves 
        moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return False
        if index == len(word):
            return len(word)
        for x, y in moves:
            letter = grid[r][c]
            if letter == word[index] and if_word_exists(grid, word, r+x, c+y, index+1):
                return True
    
    # Verifing that grid and list of word exist
    if not grid and words or grid and not words or not grid and not words:
        return 'Please provide valid grid and list of words'

    max_length = 0
    try:
        for word in words:
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if if_word_exists(grid, word, r, c, 0):
                        if len(word) > max_length:
                            max_length = len(word)
                            longest_word = word
        return longest_word
    except:
        return 'No words in Grid'

# words = ['forthhh', 'fortranhh', 'fortranhhh']
# words = []
# words = scraping.word_list

# grid3 = []

# grid = [['Q', 'W', 'E', 'R', 'T', 'N', 'U', 'I'],
#         ['O', 'P', 'A', 'A', 'D', 'F', 'G', 'H'],
#         ['T', 'K', 'L', 'Z', 'X', 'C', 'V', 'B'],
#         ['N', 'M', 'R', 'W', 'F', 'R', 'T', 'Y'],
#         ['U', 'I', 'O', 'P', 'A', 'S', 'D', 'F'],
#         ['G', 'H', 'J', 'O', 'L', 'Z', 'X', 'C'],
#         ['V', 'B', 'N', 'M', 'Q', 'W', 'E', 'R'],
#         ['T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S']]



# grid2 = [['E', 'X', 'T', 'R', 'A', 'H', 'O', 'P'],
#         ['N', 'E', 'T', 'W', 'O', 'R', 'K', 'S'],
#         ['Q', 'I', 'H', 'A', 'C', 'I', 'Q', 'T'],
#         ['L', 'F', 'U', 'N', 'U', 'R', 'X', 'B'],
#         ['B', 'W', 'D', 'I', 'L', 'A', 'T', 'V'],
#         ['O', 'S', 'S', 'Y', 'N', 'A', 'C', 'K'],
#         ['Q', 'W', 'O', 'P', 'M', 'T', 'C', 'P'],
#         ['K', 'I', 'P', 'A', 'C', 'K', 'E', 'T']]


# print(find_longest_word(grid2, words))

