from stats import get_num_words, get_character_count, sort_characters
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book = get_book_text(sys.argv[1])
    num_words = get_num_words(book)
    char_dict = get_character_count(book)
    sorted_dict = sort_characters(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_dict:
        ch = item["char"]
        count = item["num"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {count}")        
    print("============= END ===============")

if __name__ == "__main__":
    main()
