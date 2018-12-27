import html_scraping

def find_longest_word(grid, words):

    def if_word_exists(grid, word, row, col, index):
        """
        Recursive function to verify that the candidate word exists in the grid
        """
        word = word.upper()        
        # Valid chess knight moves 
        moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return False
        if index == len(word):
            return True

        for x, y in moves:
            letter = grid[row][col]
            # print(f'letter: {letter}, word index: {word[index]}, index: {index}, row: {row}, col: {col}')
            if letter != word[index]:
                return False

            if letter == word[index] and if_word_exists(grid, word, row+x, col+y, index+1):
                return True


    # Verifing that grid and list of word exist
    if not grid and words or grid and not words or not grid and not words:
        return 'Please provide valid grid and/or list of words'

    max_length = 0
    try:
        for word in words:
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if if_word_exists(grid, word, row, col, 0):
                        if len(word) > max_length:
                            max_length = len(word)
                            longest_word = word
        return longest_word
    except:
        return 'No words could be produced by this Grid'

# grid = [['Q', 'W', 'E', 'R', 'T', 'N', 'U', 'I'],
#         ['O', 'P', 'A', 'A', 'D', 'F', 'G', 'H'],
#         ['T', 'K', 'L', 'Z', 'X', 'C', 'V', 'B'],
#         ['N', 'M', 'R', 'W', 'F', 'R', 'T', 'Y'],
#         ['U', 'I', 'O', 'P', 'A', 'S', 'D', 'F'],
#         ['G', 'H', 'J', 'O', 'L', 'Z', 'X', 'C'],
#         ['V', 'B', 'N', 'M', 'Q', 'W', 'E', 'R'],
#         ['T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S']]
	
# words = ['wlph']

# print(find_longest_word(grid, words))