#include <Windows.h>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <string>
using namespace std;

char byte_3004[] = { 0x44, 0xF6, 0xF5, 0x57, 0xF5, 0xC6, 0x96, 0xB6, 0x56, 0xF5,
					 0x14, 0x25, 0xD4, 0xF5, 0x96, 0xE6, 0x37, 0x47, 0x27, 0x57,
					 0x36, 0x47, 0x96, 3, 0xE6, 0xF3, 0xA3,0x92, 0 };

int __fastcall sub_2494(unsigned __int8 a1, int a2)
{
	int v3; // [sp+8h] [bp-8h]@1
	int i; // [sp+Ch] [bp-4h]@1

	v3 = a1; // v3 = input_key's byte ASCII code
	for (i = 0; i < a2; ++i) //a2 = 1
	{
		v3 *= 2;
		if (v3 & 0x100)
			v3 |= 1u;
	}
	return (unsigned __int8)v3;
}

signed __int32 __fastcall sub_232C(signed __int32 result, int a2)
{
	int v2; // [sp+0h] [bp-14h]@1
	char *v3; // [sp+4h] [bp-10h]@1
	int i; // [sp+8h] [bp-Ch]@1
	signed __int32 j; // [sp+Ch] [bp-8h]@2

	v3 = (char *)result; //input_key's address
	v2 = a2; // v2 = 4
	for (i = 0; i < v2; ++i)
	{
		for (j = 0; ; ++j)
		{
			result = strlen(v3);
			if (result <= j)
				break;
			v3[j] = sub_2494(v3[j], 1); // sub2494(input_key's string, 1)
		}
	}
	return result;
}
int sub_2224()
{
	char v1; // [sp+4h] [bp-5Ch]@1
	int v2; // [sp+54h] [bp-Ch]@1
	signed __int32 v3; // [sp+58h] [bp-8h]@1
	signed __int32 i; // [sp+5Ch] [bp-4h]@1
	char vars0; // [sp+60h] [bp+0h]@2

	v2 = 4;
	printf("Input key : ");
	scanf("%s", &v1);
	v3 = strlen(&v1);
	sub_232C((signed __int32)&v1, v2); //sub_232C(input_key, 4);
	for (i = 0; i < v3; ++i)
	{
		if ((unsigned __int8)*(&vars0 + i - 92) != byte_3004[i])
		{
			puts("Wrong Key! ");
			return 0;
		}
	}
	puts("Correct Key! ");
	return 0;
}
int main() {
	char v3;
	int check = 0;
	for (int i = 0; i < 28; i++) {
		check = 0;
		for (int j = 0x20; j < 0x80; j++) {
			v3 = j;
			for (int k = 0; k < 4; k++) {
				v3 = sub_2494(v3, 1);
			}
			if (v3 == byte_3004[i]){
				printf("%c", j);
				check = 1;
				break;
			}

		}
		if (check == 0) {
			cerr << "Error : " << i << endl;
		}
			
	}
}