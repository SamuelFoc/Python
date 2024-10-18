#include "PyInt.h"

int main() {
    int64_t num = -1234567890123456789;  // Large number to test.
    PyInt py_int(num);                   // Create an instance of PyInt.

    std::cout << "Python-style integer representation:" << std::endl;
    py_int.print();                      // Print the PyInt representation.

    std::cout << "Memory footprint: " << py_int.get_memory_footprint() << " bytes" << std::endl;

    return 0;
}