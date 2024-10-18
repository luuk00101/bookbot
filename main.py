def load_text(book_path):
    with open(book_path) as book:
        return book.read()


def get_word_count(text):
    return len(text.split())


def get_character_count(text):
    text = text.lower()

    character_dict = {}

    for character in text:
        if not character.isalpha():
            continue
        elif character_dict.get(character):
            character_dict[character] += 1
        else:
            character_dict[character] = 1

    return character_dict

def dict_to_sorted_list(dictionary):
    list = []

    for key in dictionary:
        list.append([key, dictionary[key]])
 
    list.sort(reverse=True, key=lambda x:x[1])

    return list

def print_report(book_path, text):
    print(f"--- Begin report of {book_path} ---")

    word_count = get_word_count(text)
    print(f"{word_count} words found in the document\n")

    character_dict = get_character_count(text)
    sorted_list = dict_to_sorted_list(character_dict)
    for value in sorted_list:
        print(f"The '{value[0]}' character was found {value[1]} times")

    print("--- End report ---")


def main():
    book_path = "books/frankenstein.txt"
    text = load_text(book_path)
    print_report(book_path, text)


main()
