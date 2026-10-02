#include <iostream>

int main() {
    int num;
    std::cout << "Введите число: ";
    std::cin >> num;

    if (num % 2 == 0) {
        std::cout << "Число" << num << " - чётное.\n";
    } else {
        std::cout << "Число" << num << " - нечётное.\n";
    }

    return 0;
}