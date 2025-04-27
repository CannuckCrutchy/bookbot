from stats import *
import sys

#Lesson 3 Reading a file
def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

#First version of main related to Lesson 3
#def main():
#    book = get_book_text('books/frankenstein.txt')
#    print (book)

#Lesson 4 Count Words function 'word_count" moved to stats.py in later lesson

#main function is segmented to show related work from each lesson, so prints were grouped with the new material
#Now that a report is needed the print statements will be properly placed at the bottom 
def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print(f"Book file path provided: {book_path}")
    #Lesson 4 Count Words
    #Thought the line below no longer needed now that bookpath is a variable but it is
    book = get_book_text(book_path)
    num_words = word_count(book)
    #print(f'{num_words} words found in the document')
    
    char_count = letter_county(book)
    #print ("How often each character appears in the file:")
    #print(char_count)

    sorted_counts = sorted_count(char_count)
    #print("Sorted character counts (most frewuent first:):")
    #for char_info in sorted_counts:
    #    print(f"Character: {char_info['char']} - Count: {char_info['num']}")


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")
    for char_info in sorted_counts:
        print(f"{char_info['char']}: {char_info['num']}")
    print("============= END ===============")

main()

