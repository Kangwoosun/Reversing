#include <stdio.h>

int main()
{
	int firsteax = 0xB7AAC296, nexteax = 0x5A5A7E05;
	int temp = 0, i = 0;
	while (1)
	{
		_asm
		{
			mov eax, firsteax
			mov cl, al
			mov ebx, i
			rol ebx, cl
			xor eax, ebx
			mov cl, bh
			ror eax, cl
			add ebx, eax
			mov temp, eax
		}
		if (temp == nexteax)
			printf("0x%08x\n", i);

		if (i == 0xffffffff)
			break;

		i++;
	}
	return 0;
}