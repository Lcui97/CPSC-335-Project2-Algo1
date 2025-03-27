# ----------------------------------------------------
# main.py
# ----------------------------------------------------
from search_substrings import find_target_substrings

def main():
    # 1. Read the single large string from in2a.txt
    with open('in2a.txt', 'r', encoding='utf-8') as f:
        concatenated_str = f.read().strip()
    
    # 2. (Optional) Read the list of target words from in2b.txt
    #    If you do NOT have in2b.txt, you can just hardcode the list B.
    try:
        with open('in2b.txt', 'r', encoding='utf-8') as f:
            B = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        # Fallback if in2b.txt doesn't exist
        B = ["oakland", "rialto", "full", "marco", "clovis"]
    
    # 3. Call the search routine
    indices, words = find_target_substrings([concatenated_str], B)
    
    # 4. Print results
    print("Indices:", indices)
    print("Words:  ", words)

if __name__ == '__main__':
    main()
