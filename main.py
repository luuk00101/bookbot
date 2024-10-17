def load_text():
    with open("books/frankenstein.txt") as book:
        return book.read()


def get_word_count(text):
    return len(text.split())


def main():
    text = load_text()
    print(get_word_count(text))


main()
