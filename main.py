import pathlib
import sys
from stats import get_word_count, get_character_stats, sort_character_stats

def main():
    print("============ BOOKBOT ============")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file = pathlib.Path(sys.argv[1])
    print(f"Analyzing book found at {file}...")
    text = get_book_text(file=file)
    print("----------- Word Count ----------")
    word_count = get_word_count(text=text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    charater_stats = sort_character_stats(get_character_stats(text=text))
    for char_stat in charater_stats:
        if char_stat["char"].isalpha():
            print(f"{char_stat["char"]}: {char_stat["num"]}")
    print("============= END ===============")

def get_book_text(file: pathlib.Path):
    return file.read_text()

main()