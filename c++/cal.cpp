// calculator.cpp - Source file
#include "cal.h"

cal::cal() {}

int cal::add(int num1, int num2) {
    return num1 + num2;
}

int cal::subtract(int num1, int num2) {
    return num1 - num2;
}

int cal::multiply(int num1, int num2) {
    return num1 * num2;
}

double cal::divide(int num1, int num2) {
    if (num2 == 0) {
        // Check for division by zero
        return 0.0; // You can handle this differently if needed
    }
    return static_cast<double>(num1) / num2;
}
