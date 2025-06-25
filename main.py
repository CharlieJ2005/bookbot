from stats import get_num_words, get_num_chars, get_num_chars_sorted
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]


book_text = get_book_text(book_path)
num_words = get_num_words(book_text)
num_chars = get_num_chars(book_text)
num_chars_sorted = get_num_chars_sorted(num_chars)


print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")
for entry in num_chars_sorted:
    if entry["char"].isalpha():
        print(f"{entry["char"]}: {entry["num"]}")
print("============= END ===============")
