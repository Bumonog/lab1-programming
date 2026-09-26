#include <iostream>
#include <string>
#include <typeinfo>

int main() {
    int num_int;
    double num_float;
    std::string text;

    std::cout << "Введите число: ";
    std::cin >> num_int;

    std::cout << "Введите дробное число: ";
    std::cin >> num_float;

    std::cin.ignore(); // очистил буфер

    std::cout << "Введите строку: ";
    std::getline(std::cin, text);

    std::cout << "Значение: " << num_int
              << ", тип: " << typeid(num_int).name() << "\n";
    std::cout << "Значение: " << num_float
              << ", тип: " << typeid(num_float).name() << "\n";
    std::cout << "Значение: " << text
              << ", тип: " << typeid(text).name() << "\n";

    return 0;
}