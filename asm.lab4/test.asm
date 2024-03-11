.686P
.model flat, c
.code

sum		proc a:dword, b:dword
			mov eax, a
			add eax, b
			ret
sum		endp
end