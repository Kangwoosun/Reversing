# -*- coding: utf-8 -*-
#한글 인식이 안되서 붙여주는 전처리기
import os, sys
import random
import struct

print "* polymorphic XOR Shellcode Encoder by hyunmini * \n"

def xor(data, key):
	leng = len(key)
	xor1 = ""
	reverse = ""
	for i in range(0, len(data)):
		reverse += struct.pack("B", (ord(data[i]) ^ ord(key[i % leng])))

	return reverse

def conv_hex(data):
	hex_str = ""
	for i in range(0, len(data)):
		hex_str += ("0x%02x" %ord(data[i])).replace('0x', '\\x')

	return hex_str

org_shellcode = (
	"\x41\x41\x41\x41\x42\x42\x42\x42\x43\x43\x43\x43\x44\x44\x44\x44"
)
xor_key = os.urandom(4)

decoder1 = "\xe8\xff\xff\xff\xff\xc2\x5e"				  #GetPC
decoder2 = "\x6a" + chr(len(org_shellcode)/4 + 1) + "\x59"#Counter
decoder3 = "\xbf" + xor_key								  #XOR Key

decoder_rand = [decoder1, decoder2, decoder3]
random.shuffle(decoder_rand)				 
decoder = "".join(decoder_rand)				 
#GetPC, Counter, XOR Key의 순서를 랜덤화

getpc_offset = len(decoder) - decoder.index(decoder1) + 3
#decoder의 크기에서 GetPC의 위치를 빼주고 GetPC중 call + 4부분에 대한 기계어크기를
#빼주고 아래의 decoder4의 크기(8)을 더해주면 +3이 됨
decoder4_1 = "\x31\x7e" + chr(getpc_offset)
decoder4_2 = "\x83\xc6\x04"
decoder4_3 = "\xe2\xf8"
decoder4 = decoder4_1+ decoder4_2 + decoder4_3

decoder += decoder4

xor_shellcode = xor(org_shellcode, xor_key)
print "Orginal : " + conv_hex(org_shellcode) + '\n'
print "Encoded : " + conv_hex(decoder) + conv_hex(xor_shellcode) + '\n'