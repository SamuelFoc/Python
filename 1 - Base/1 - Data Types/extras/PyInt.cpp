#include "PyInt.h"

// Constructor: Convert a normal int64_t to the PyInt representation.
PyInt::PyInt(int64_t value) {
    is_negative = value < 0;
    if (is_negative) {
        value = -value;  // Work with the absolute value.
    }

    // Split the value into chunks of 30 bits.
    while (value > 0) {
        digits.push_back(value % BASE);  // Store the least significant 30 bits.
        value /= BASE;                   // Shift right by 30 bits.
    }
    if (digits.empty()) {
        digits.push_back(0);  // Handle the case where value is zero.
    }
}

// Print function: Print the integer for debugging.
void PyInt::print() const {
    if (is_negative) {
        std::cout << "-";
    }
    for (int i = digits.size() - 1; i >= 0; --i) {
        std::cout << digits[i];
        if (i > 0) std::cout << " "; // Print a space between "digits".
    }
    std::cout << std::endl;
}

// Memory footprint function: Returns the memory usage of the PyInt object.
size_t PyInt::get_memory_footprint() const {
    return sizeof(PyInt) + digits.size() * sizeof(uint32_t);
}