import pytest
from longest_word_solution import find_longest_word
import html_scraping


def test_find_longest_word_exists():
	"""
	Test verifies that find longest word fanction exsits
	"""
	assert find_longest_word


def test_if_no_grid_or_no_words_provided():
	"""
	test returns if no grid or no word list is provided
	"""
	assert find_longest_word([], []) == 'Please provide valid grid and/or list of words'
	assert find_longest_word(['A', 'B', 'C'], []) == 'Please provide valid grid and/or list of words'
	assert find_longest_word([], ['extrahop', 'TCP']) == 'Please provide valid grid and/or list of words'


def test_with_8by8_grid_and_word_list():
	"""
	test if function return the longest word from a list 
	if multiple words can be produced
	"""
	grid = [['Q', 'W', 'E', 'R', 'T', 'N', 'U', 'I'],
        ['O', 'P', 'A', 'A', 'D', 'F', 'G', 'H'],
        ['T', 'K', 'L', 'Z', 'X', 'C', 'V', 'B'],
        ['N', 'M', 'R', 'W', 'F', 'R', 'T', 'Y'],
        ['U', 'I', 'O', 'P', 'A', 'S', 'D', 'F'],
        ['G', 'H', 'J', 'O', 'L', 'Z', 'X', 'C'],
        ['V', 'B', 'N', 'M', 'Q', 'W', 'E', 'R'],
        ['T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S']]
	
	words = ['algol', 'fortran', 'fort']
	assert find_longest_word(grid, words) == 'fortran'


def test_with_no_words_found_in_grid():
	"""
	Test function return if no words for a list can be produced by the grid
	"""
	grid = [['Q', 'W', 'E', 'R', 'T', 'N', 'U', 'I'],
        ['O', 'P', 'A', 'A', 'D', 'F', 'G', 'H'],
        ['T', 'K', 'L', 'Z', 'X', 'C', 'V', 'B'],
        ['N', 'M', 'R', 'W', 'F', 'R', 'T', 'Y'],
        ['U', 'I', 'O', 'P', 'A', 'S', 'D', 'F'],
        ['G', 'H', 'J', 'O', 'L', 'Z', 'X', 'C'],
        ['V', 'B', 'N', 'M', 'Q', 'W', 'E', 'R'],
        ['T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S']]
	
	words = ['algols', 'fortransshh', 'simulass']
	assert find_longest_word(grid, words) == 'No words could be produced by this Grid'


def test_if_function_return_correct_longest_word_from_Shakespeare_play():
	"""
	"""
	grid = [['E', 'X', 'T', 'R', 'A', 'H', 'O', 'P'],
        ['N', 'E', 'T', 'W', 'O', 'R', 'K', 'S'],
        ['Q', 'I', 'H', 'A', 'C', 'I', 'Q', 'T'],
        ['L', 'F', 'U', 'N', 'U', 'R', 'X', 'B'],
        ['B', 'W', 'D', 'I', 'L', 'A', 'T', 'V'],
        ['O', 'S', 'S', 'Y', 'N', 'A', 'C', 'K'],
        ['Q', 'W', 'O', 'P', 'M', 'T', 'C', 'P'],
        ['K', 'I', 'P', 'A', 'C', 'K', 'E', 'T']]
	
	words = html_scraping.word_list
	assert find_longest_word(grid, words) == 'honorificabilitudinitatibus'