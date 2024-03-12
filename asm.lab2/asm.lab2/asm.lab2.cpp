#include <iostream>

int main()
{
	//first task
	int x, res1, res2, res, y = 2, number, ten = 10, sum = 0;
	std::cin >> x >> number;
	_asm {
		mov eax, x
		mov cx, 5
		start:
		imul x
			dec cx
			cmp cx, 0
			je finish
			jmp start
		finish:
		mov res1, eax
			mov eax, x
			imul x
			sub eax, 4
			imul y
			mov res2, eax
			add eax, res1
			add eax, x
			idiv x
			idiv x 
			cdq
			idiv x 
			mov res, eax
	}
	std::cout << "Value of expression: ";
	std::cout << res << std::endl;
	std::cout << "----------------------------------------" << std:: endl;
	//second task
	_asm {
		mov eax, number
		start1:
		cdq
		idiv ten
			add sum, edx
			cmp eax, 0
			je finish1
			jmp start1
			finish1:
	}
	std::cout << "Sum of digits of a number: ";
	std::cout << sum << std::endl;
	return 0;
}
