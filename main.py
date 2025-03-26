# ----------------------------------------------------
# main.py
# ----------------------------------------------------
from search_substrings import find_target_substrings

def main():
    # Read the single large string from in2a.txt
    with open('in2a.txt', 'r', encoding='utf-8') as f:
        concatenated_str = f.read().strip()
    
    # Call the search routine
    indices, words = find_target_substrings([concatenated_str], B)
    
    # 4. Print results
    print("Indices:", indices)
    print("Words:  ", words)

if __name__ == '__main__':
    main()
