def count_words(*, text: str) -> int:
    for char in ",.?/\\|~`!@#$%^&*()_+=-:;'\"":
        text = text.replace(char, " ")
    print(text)
    print(text.split())
    return len(text.split())

text = input("Enter the text: ")
words = count_words(text=text)

print(f"This text has {words} words.")

