def load_text():
    with open("books/frankenstein.txt") as book:
        return book.read()


def get_word_count(text):
    return len(text.split())


def get_character_count(text):
    text = text.lower()

    character_dict = {}

    for character in text:
        if character_dict.get(character):
            character_dict[character] += 1
        else:
            character_dict[character] = 1

    return character_dict


def main():
    text = load_text()
    print(get_word_count(text))
    print(get_character_count(text))


main()
