import html_scraping

def find_longest_word(grid, words):
    """
    This main function takes a grid of letters and a list of words and 
    returns the longest word from the list that can be produced from the grid
    """
    
    if not grid or not words:
        return 'Please provide valid grid and/or list of words'

    def if_word_exists(word, row, col, index):
        """
        Helper recursive function that take a word and verifies 
        that this candidate word could be produced from the grid
        """
        word = word.upper()        
        moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        
        if index == len(word):
            return True
        if not 0 <= row < len(grid) or not 0 <= col < len(grid[0]):
            return False

        for x, y in moves:
            letter = grid[row][col]
            if letter != word[index]:
                return False
            if letter == word[index] and if_word_exists(word, row + x, col + y, index + 1):
                return True
  
    
    max_length = 0
    try:
        for word in words:
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if if_word_exists(word, row, col, 0):
                        if len(word) > max_length:
                            max_length = len(word)
                            longest_word = word
        return longest_word
    except:
        return 'No words could be produced by this Grid'
