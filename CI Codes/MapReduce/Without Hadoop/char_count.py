import sys

def count_characters(input_file):
    char_count = {}
    with open(input_file, 'r') as file:
        for line in file:
            line = line.lower().replace(" ", "")
            for char in line:
                if char.isalpha():  # Ignore non-alphabet characters
                    char_count[char] = char_count.get(char, 0) + 1
    return char_count

def main():
    if len(sys.argv) < 2:
        print("Usage: python char_count_simple.py <input-file>")
        return

    input_file = sys.argv[1]
    char_count = count_characters(input_file)

    # Print character counts
    for char, count in char_count.items():
        print(f"{char}: {count}")

if __name__ == "__main__":
    main()