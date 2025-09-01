from stats import count_words
from stats import count_characters
from stats import sort_list
import sys

def get_book_text(path_to_file):    #accepts path, returns book contents as string
    with open(path_to_file) as contents:
        return contents.read()

def print_report(final_word_count, final_character_count, final_sorted_list, final_path_to_file):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {final_path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {final_word_count} total words")
    print("--------- Character Count -------")
    for dictionaries in final_sorted_list:
        if dictionaries["char"].isalpha():
            print(f"{dictionaries["char"]}: {dictionaries["num"]}")
    print("============= END ===============")




def main():
    print(sys.argv)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_file = sys.argv[1]


    word_count = count_words(get_book_text(path_to_file))
    character_count = count_characters(get_book_text(path_to_file))
    sorted_list = sort_list(character_count)
    print_report(word_count, character_count,sorted_list,path_to_file)




main()