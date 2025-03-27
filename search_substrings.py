# search_substrings.py

def find_substring_indices(text, pattern):
    """
    Returns the starting index of 'pattern' in 'text' (first occurrence),
    or -1 if not found. This is a naive approach.
    """
    n = len(text)
    m = len(pattern)
    for start in range(n - m + 1):
        if text[start:start + m] == pattern:
            return start
    return -1

def find_target_substrings(A, B):
    """
    A: list containing one concatenated string.
    B: list of target words.
    
    Returns:
      indices_list: list of integer positions where each target word appears.
      words_list:   list of the corresponding target words (in order of occurrence).
    """
    concatenated_string = A[0]
    found_pairs = []  # List to store tuples (index, word)

    for word in B:
        index_found = find_substring_indices(concatenated_string, word)
        if index_found != -1:
            found_pairs.append((index_found, word))
    
    # Sort the pairs by index so that results are in the order they appear.
    found_pairs.sort(key=lambda x: x[0])
    
    indices_list = [pair[0] for pair in found_pairs]
    words_list = [pair[1] for pair in found_pairs]
    
    return indices_list, words_list
