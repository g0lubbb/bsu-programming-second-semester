#include <iostream>
extern "C" int sum(int, int);
int main() {
	int a, b;
	std::cin >> a >> b;
	std::cout << sum(a,b);
}