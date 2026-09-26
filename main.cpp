#include <iostream>
#include <iomanip>

int main() {
    int seconds;
    std::cout << "Введите кол-во секунд: ";
    std::cin >> seconds;

    int hours = seconds / 3600;
    int minutes = (seconds % 3600) / 60;
    int ost_seconds = seconds % 60;

    std::cout << std::setfill('0')
              << std::setw(2) << hours << ":"
              << std::setw(2) << minutes << ":"
              << std::setw(2) << ost_seconds << "\n";

    return 0;
}