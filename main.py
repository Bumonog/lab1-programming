def caesar_ciper(*, text: str, shift: int) -> str:
    """Шифруем текст шифром Цезаря"""
    
    result = list()
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    
    return ''.join(result)

original = "Hello, World!"
encrypted = caesar_ciper(text = original, shift = 3)

print(f"Original text: {original}")
print(f"Encrypted text: {encrypted}")
        