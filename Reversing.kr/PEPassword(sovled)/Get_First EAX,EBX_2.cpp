#include <Windows.h>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

int main() {
	int firstEAX, firstEBX;

	__asm {
		MOV EDX, 0xFFD
		MOV EAX, 0x20c1085a
		MOV EBX, 0x9527AC54
		L1:
		SUB EBX,EAX
		MOV CL, BH
		ROL EAX,CL
		XOR EAX, EBX
		MOV CL, AL
		ROR EBX, CL
		DEC EDX
		JNZ L1
		MOV firstEAX, EAX
		MOV firstEBX, EBX
	}
	printf("EAX = 0x%8x\n", firstEAX);
	printf("EBX = 0x%8x\n", firstEBX);
}