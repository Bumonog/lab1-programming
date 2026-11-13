def is_palindrome(*, text: str) -> bool:
    for char in ",./?'\";:!@#$%^&*()_+=-[] `~<>":
        text = text.replace(char, '')
    text = text.lower()
    return text == text[::-1]

test_text = [
    "А роза упала на лапу Азора",
    "Madam, I'm Adam",
    "Hello, world!",
    "12321",
    "racecar"
]

for text in test_text:
    result = "palindrome" if is_palindrome(text=text) else "not polindrome"
    print(f"{text} - {result}")