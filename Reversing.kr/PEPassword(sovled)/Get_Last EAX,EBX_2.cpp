#include <Windows.h>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>


__declspec(naked) DWORD NextP(DWORD P, DWORD Q)
{
	__asm
	{
		mov eax, [esp + 4]
		mov ebx, [esp + 8]
		mov cl, al
		rol ebx, cl
		xor eax, ebx
		mov cl, bh
		ror eax, cl
		add ebx, eax
		ret
	}
}

__declspec(naked) DWORD NextQ(DWORD P, DWORD Q)
{
	__asm
	{
		mov eax, [esp + 4]
		mov ebx, [esp + 8]
		mov cl, al
		rol ebx, cl
		xor eax, ebx
		mov cl, bh
		ror eax, cl
		add ebx, eax
		mov eax, ebx
		ret
	}
}
int main()
{
//	DWORD P[] = { 0x726ee12b, 0x20c1085a, 0xae3934ca, 0x79c0c66b };
	DWORD P[] = { 0x55FCA1C9, 0x7bd6f03a, 0x726ee12b, 0x20c1085a };


	int cnt = sizeof(P) / sizeof(P[0]) - 1;

	for (int j = 0; j<cnt; ++j)
	{
		for (__int64 i = 0; i<0xffffffff; ++i)
		{
			if (NextP(P[j], (DWORD)i) == P[j + 1])
				printf("Q = %08X  NextQ = %08X\n"
					, (DWORD)i
					, NextQ(P[j], (DWORD)i));
		}

		printf("\n\n");
	}

	return 0;
}