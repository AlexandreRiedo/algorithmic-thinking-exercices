def solve():
    num_lines = int(input())
    used_words = set()

    prev_word = input()
    used_words.add(prev_word)
    for turn in range(1, num_lines):
        word = input()
        if prev_word[-1] == word[0] and word not in used_words:
            used_words.add(word)
            prev_word = word
        else:
            return f"Player {(turn % 2) + 1} lost"
    
    return "Fair Game"

if __name__ == "__main__":
    print(solve())