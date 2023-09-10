// main.cpp - Main program
#include <iostream>
#include "cal.h"

int main() {
    cal calc;
    int num1, num2;

    std::cout << "Enter two numbers: ";
    std::cin >> num1 >> num2;

    int sum = calc.add(num1, num2);
    int difference = calc.subtract(num1, num2);
    int product = calc.multiply(num1, num2);
    double quotient = calc.divide(num1, num2);

    std::cout << "Sum: " << sum << std::endl;
    std::cout << "Difference: " << difference << std::endl;
    std::cout << "Product: " << product << std::endl;
    std::cout << "Quotient: " << quotient << std::endl;

    return 0;
}
