#include <iostream>
    int main() {
        int res1, res2;
        long int res;
        int x;
        std::cin >> x;
        //first task 
        _asm {
            mov ecx, 12
            mov eax, x
            cdq
            start1 :
            imul x
                dec ecx
                cmp ecx, 1
                je finish1
                jmp start1
                finish1 :
            mov res1, eax

                mov ecx, 8
                mov eax, x
                cdq
                start2 :
            imul x
                dec ecx
                cmp ecx, 1
                je finish2
                jmp start2
                finish2 :
            mov res2, eax
                add eax, res1
                add eax, x
                mov res, eax
        }
        std::cout << res << std::endl;
        std::cout << "----------------" << std::endl;
        //second task
        int i = 0, a = 0, b = 0;
        int arr[50]{ 0 };
        _asm {
            mov ebx, i
            outer_loop :
            mov eax, a
                mov edx, b
                shl eax, 1
                imul edx, 3
                add eax, edx
                cmp eax, 50
                jne next
                mov eax, a
                mov edx, b
                mov arr[ebx], eax
                mov arr[ebx + 4], edx
                add ebx, 8

                next:
            add b, 1
                cmp b, 17
                jl outer_loop

                mov b, 0
                add a, 1;
            cmp a, 26;
            jl outer_loop

        }
        for (int i = 0; i < 9; ++i) {
            std::cout << "2*" << arr[i * 2] << " + 3*" << arr[i * 2 + 1] << " = 50" << std::endl;
        }
        std::cout << "----------------" << std::endl;
        // third task 
        int arr2[50]{ 0 };
        arr2[0] = 0;
        arr2[1] = 1;
        __asm {
            mov ecx, 2
            beg_:
            cmp ecx, 50
                je end_
                mov eax, arr2[4 * ecx - 4]
                add eax, arr2[4 * ecx - 8]
                jo end_
                mov  arr2[4 * ecx], eax
                add ecx, 1
                jmp beg_
                end_ :
        }
        for (int i = 0; i < 50; i++)
        {
            std::cout << arr2[i] << std::endl;
        }
        std::cout << "----------------" << std::endl;
        // fourth task 
        unsigned int numerator, nod, zero = 0;
        int denominator;
        std::cout << "Enter the integer numerator and natural denominator: " << std::endl;
        std::cin >> numerator >> denominator;
        if (denominator == 0) {
            std::cout << "Enter numbers that match the condition! " << std::endl;
            std::exit;
        }
        _asm {
            xor si, si
            mov eax, numerator
            mov ebx, denominator
            cmp ebx, zero
            ja start
            mov si, 1
            neg denominator
            start :
            cdq
                idiv ebx
                cmp edx, 0
                je end
                mov eax, ebx
                mov ebx, edx
                jmp start
                end :
            mov nod, ebx
                mov eax, numerator
                idiv nod
                mov numerator, eax
                mov eax, denominator
                cdq
                idiv nod
                mov denominator, eax
                cmp si, 1
                jne end1
                neg denominator
                end1:
        }
        if (numerator == denominator) {
            std::cout << "Result: ";
            std::cout << "1" << std::endl;
        }
        else {
            std::cout << "Result: ";
            std::cout << numerator << "/" << denominator;
        }
        return 0;
    }
