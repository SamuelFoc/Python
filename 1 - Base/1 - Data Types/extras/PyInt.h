#ifndef PYINT_H
#define PYINT_H

#include <iostream>
#include <vector>
#include <cstdint>

class PyInt {
private:
    std::vector<uint32_t> digits;  // Each "digit" is a 30-bit chunk of the number.
    bool is_negative;              // Sign of the integer.
    const uint32_t BASE = 1 << 30; // Left shift of 30 bits (Base 2^30).

public:
    // Constructor from a normal int64_t.
    PyInt(int64_t value);

    // Function to print the number (for debugging).
    void print() const;

    // Return the memory footprint similar to Python's int.
    size_t get_memory_footprint() const;
};

#endif