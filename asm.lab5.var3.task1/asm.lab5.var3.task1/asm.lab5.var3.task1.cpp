#include <iostream>

int main()
{
    int k = 1, i, res1, one = 1, two = 2;
    float sum = 0, sum_element, res, eight = 8, pi = 3.14159;
    std::cout << "Enter number of iterations: " << std::endl;
    std::cin >> i; // entering the number of iterations
    _asm {
    start:
        mov ebx, i
            mov ecx, k
            cmp ecx, ebx
            jg end
            fild k
            fimul two
            fisub one
            fistp res1
            fld one
            fdiv res1
            fstp sum_element
            fld sum_element;       finding the sum element
            fld sum
            fadd
            fstp sum
            fild k
            fiadd one
            fistp k
            jmp start


            end :
        fldpi
            fmul pi
            fdiv eight
            fstp res;       finding the value of pi
    }
    std::cout << "Sum value: " << std::endl;
    std::cout << sum << std::endl;
    std::cout << "----------" << std::endl << "Pi value: " << std::endl;
    std::cout << res << std::endl;
    return 0;
}