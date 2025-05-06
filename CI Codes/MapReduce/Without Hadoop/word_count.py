import sys
import re
from collections import defaultdict

def count_words(input_file):
    word_count = defaultdict(int)
    with open(input_file, 'r') as file:
        for line in file:
            words = re.findall(r'\w+', line.lower())  # Extract words and ignore non-word characters
            for word in words:
                word_count[word] += 1
    return word_count

def main():
    if len(sys.argv) < 2:
        print("Usage: python word_count_simple.py <input-file>")
        return

    input_file = sys.argv[1]
    word_count = count_words(input_file)

    # Print word counts
    for word, count in word_count.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()