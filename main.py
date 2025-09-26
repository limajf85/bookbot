from stats import get_book_text, count_words, count_chars, sort_dict
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_counts = count_chars(book_text)
    sorted_chars = sort_dict(char_counts)

    header = f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...\n----------- Word Count ----------"
    footer = "============= END ==============="

    print(header)
    print(f"Found {word_count} total words\n--------- Character Count -------")

    for d in sorted_chars:
        print(f"{d['char']}: {d['num']}")
    print(footer)

main()