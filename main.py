def sort_on(dict):
    return dict["name"]


def main():
    book = "./books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read().lower()

        words = file_contents.split()
        print(len(words))

        letter_dict = {}

        for letter in file_contents:
            if letter not in letter_dict:
                letter_dict.update({letter: 1})
            else:
                current_number = letter_dict[letter]
                current_number += 1
                letter_dict.update({letter: current_number})

        print(letter_dict)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")
    print()
    records = [{"name": key, "num": value} for key, value in letter_dict.items()]
    records.sort(key=sort_on)

    for item in records:
        if item.get("name").isalpha():
            print(f"The '{item.get('name')}' letter was found {item.get('num')} times")

    print("--- End report ---")


if __name__ == "__main__":
    main()
