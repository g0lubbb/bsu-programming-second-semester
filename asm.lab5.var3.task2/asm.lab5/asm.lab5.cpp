#include <iostream>

int main()
{
    float n;
    float k = 2;
    float one = 1;
    float minus_one = -1;
    float x;
    float res;
    float log;
    float sum = 0;
    float abs_x;

    float temp;

    std::cout << "Enter x: " << std::endl;
    std::cin >> x;
    std::cout << "Enter number of iterations: " << std::endl;
    std::cin >> n;
    _asm {
        mov ecx, n
        fld x
        fsub one
        fst abs_x
        fstp x
        start :
        mov ebx, k
            cmp ebx, ecx
            jg end
            fld x
            fmul abs_x
            fmul minus_one
            fstp x
            fld x
            fdiv k
            fstp res
            fld sum
            fadd res
            fstp sum
            fld k
            fadd one
            fstp k
            jmp start
            end :
        fld sum
            fadd one
            fstp sum
    }
    std::cout << sum << std::endl;
    _asm {
        fldln2
        fstp log
    }
    std::cout << "ln2: ";
    std::cout << log << std::endl;
    return 0;
}