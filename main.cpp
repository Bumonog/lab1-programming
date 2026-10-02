#include <iostream>

int main() {
    int age;
    std::cout << "Введите возраст: ";
    std::cin >> age;

    if (age < 0) {
        std::cout << "некорректный возраст\n";
    } else if (age <= 12) {
        std::cout << "ребёнок\n";
    } else if (age <= 17) {
        std::cout << "подросток\n";
    } else if (age <= 64) {
        std::cout << "взрослый\n";
    } else {
        std::cout << "пожилой";
    }

    return 0;
}