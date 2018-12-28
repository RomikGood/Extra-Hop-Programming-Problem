import html_scraping

def find_longest_word(grid, words):
    """
    This main function takes a grid of letters and a list of words and 
    returns the longest word from the list that can be produced from the grid
    """

    def if_word_exists(grid, word, row, col, index):
        """
        Recursive function to verify that the candidate word can be produced from the grid
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
            if letter != word[index]:
                return False
            if letter == word[index] and if_word_exists(grid, word, row+x, col+y, index+1):
                return True

    if not grid or not words:
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
