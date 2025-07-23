import sys
from stats import get_num_words, get_num_characters, get_report

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(get_num_words(get_book_text(f"{sys.argv[1]}")))
    print("--------- Character Count -------")
    for info in get_report(get_num_characters(get_book_text(f"{sys.argv[1]}"))):
        print(f"{info["char"]}: {info["num"]}")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()