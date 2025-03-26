# ----------------------------------------------------
# search_substrings.py
# ----------------------------------------------------
def find_substring_indices(text, pattern):
    """
    Returns the starting index of 'pattern' in 'text' (first occurrence),
    or -1 if not found. (Naive approach)
    """
    t_len = len(text)
    p_len = len(pattern)
    
    for start in range(t_len - p_len + 1):
        match = True
        for i in range(p_len):
            if text[start + i] != pattern[i]:
                match = False
                break
        if match:
            return start
    return -1

def find_target_substrings(A, B):
    """
    A: array with exactly one element - a long concatenated string
    B: array of target words
    Returns:
      indices_list: list of integer positions where each target word appears
      words_list:   list of the actual matched words in order of appearance
    """
    concatenated_string = A[0]  # Single large string
    found_pairs = []           # Will store tuples of (index, word)

    for word in B:
        index_found = find_substring_indices(concatenated_string, word)
        if index_found != -1:
            found_pairs.append((index_found, word))
    
    # Sort by the index
    found_pairs.sort(key=lambda x: x[0])
    
    # Separate out indices and words in order
    indices_list = [pair[0] for pair in found_pairs]
    words_list   = [pair[1] for pair in found_pairs]
    
    return indices_list, words_list
