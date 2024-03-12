#include <iostream>
int main()
{
    __int16 a1, a2, a3, b1, b2, b3, c1, c2, c3;
    std::cin >> a1 >> a2 >> a3 >> b1 >> b2 >> b3;
    long long res = 0;
    _asm {
        mov ax, a1
        add ax, b1
        mov c1, ax
        mov ax, a2
        add ax, b2
        mov c2, ax
        mov ax, a3
        add ax, b3
        mov c3, ax
    }
    std::cout << std::uppercase << std::hex << c3 << std::endl;
    std::cout << std::uppercase << std::hex << c2 << std::endl;
    std::cout << std::uppercase << std::hex << c1 << std::endl;
    std::cout << "-------------------------------" << std::endl;


    res += (static_cast<long long>(c3) << 32) + (static_cast<long long>(c2) << 16) + (static_cast<long long>(c1));
    std:: cout << std:: dec << res;
    return 0;
}