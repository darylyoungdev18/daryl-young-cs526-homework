"""
Given is a sequence of n symbols, each of which is either a dot (.) or a dash (-). This can represent a sequence of letters in Morse code. However, since the separation between letters is not given, it can represent a number of different sequences. For example, . - - could represent ETT, AT, EM, or W. 
Design an algorithm that computes the number of possible letter sequences containing only vowels (A,E,I,O,U) that can be derived from a given input sequence of dots and dashes of length n.

You should submit a readme.txt file with an explanation of your code and algorithms. You must provide exact instructions on how to run your code and you must submit screen shots of your running code. Your code should print the following text:
File Input: vowel_input<input file number>.txt 
The Number of Vowel combinations is:  <the number of combinations you calculate>
"""


"""
problem should be solved using a conceptual matrix where the top of the matric is the input morse code and the side of the matrix is the possible vowels that can be formed
look forward to see if a vowel can be formed look backwards to see how many ways you could have gotten there
"""
morse_code_vowels = {
    'A': '.-',
    'E': '.',
    'I': '..',
    'O': '---',
    'U': '..-'
}

def count_vowel_combinations(morse_sequence: str) -> int:
    """
    Count number of ways to partition morse_sequence into vowel Morse codes (A,E,I,O,U).
    Uses a straightforward DP where dp[pos] is number of ways to parse the first pos symbols.
    """
    length = len(morse_sequence)
    vowel_codes = list(morse_code_vowels.values())  # ['.-', '.', '..', '---', '..-']

    # dp[pos] = number of ways to parse morse_sequence[:pos]
    dp = [0] * (length + 1)
    dp[0] = 1  # one way to parse empty prefix

    for pos in range(1, length + 1):
        total_here = 0
        # try each vowel code that could end at position pos
        for code in vowel_codes:
            code_len = len(code)
            if pos >= code_len and morse_sequence[pos - code_len:pos] == code:
                total_here += dp[pos - code_len]
        dp[pos] = total_here

    return dp[length]


if __name__ == "__main__":
    import sys
    from pathlib import Path

    raw_text = ""
    input_name = "stdin"
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
        input_name = input_path.name
        raw_text = input_path.read_text()
    else:
        raw_text = sys.stdin.read()

    # If first line is an integer (length), ignore it. Keep only '.' and '-' from remaining lines.
    lines = raw_text.splitlines()
    if lines and lines[0].strip().isdigit():
        lines = lines[1:]
    morse_sequence = "".join(ch for line in lines for ch in line if ch in ".-")

    if not morse_sequence:
        print("No morse symbols ('.' or '-') found in input.")
        sys.exit(1)

    result = count_vowel_combinations(morse_sequence)
    print(f"File Input: {input_name}")
    print(f"The Number of Vowel combinations is: {result}")



    """
    the heart of the algorithm is finding the number of 
    combinations based on the characters that exist in the input
    we look ahead of the character to verify wheter or not our character is a vowel
    then we look back to see how many combinations leads us to the vowel. To get here 
    we ask ourself how many ways can we get to this vowel based on the previous characters

    make sure to include a start state for the algorithm 
    
    """