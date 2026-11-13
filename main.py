import re


def validate_email(email: str) -> bool:
    """Проверяет корректность email"""
    
    pattern = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """Проверяет корректность Российского телефонного номера"""
    
    pattern = r"^\+?7[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}$"
    return bool(re.match(pattern, phone))


def validate_url(url: str) -> bool:
    """Проверяет корректность url-адреса"""
    
    pattern = r"^https?://[\w.-]+\.[a-zA-Z]{2,}(/[\w./-]*)?$"
    return bool(re.match(pattern, url))


tests = [
    ("email", "ivan@example.com", validate_email),
    ("email", "invalid@", validate_email),
    ("phone", "+7 (999) 123-45-67", validate_phone),
    ("url", "https://example.com", validate_url),
    ("url", "not-a-url", validate_url),
]

for type_, value, validator in tests:
    result = "valid" if validator(value) else "not valid"
    print(f"{type_} {value} : {result}")