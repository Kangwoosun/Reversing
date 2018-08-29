key = 0

key_code = [ 0x44, 0xF6, 0xF5, 0x57, 0xF5, 0xC6, 0x96, 0xB6, 0x56, 0xF5,  0x14, 0x25, 0xD4, 0xF5,\
      0x96, 0xE6, 0x37, 0x47, 0x27, 0x57, 0x36, 0x47, 0x96, 3, 0xE6, 0xF3, 0xA3,0x92, 0 ]

input_keycode = []

for i in range(0, 29):
    check = 0
    for j in range(0x20, 0x80):
        key = j
        for k in range(0, 4):
            key *= 2
            if (key & 0x100) :
                key |= 1
    if (key == key_code[i]):
        input_keycode.insert(i,key)
        check = 1
        break

    if check == 0:
        print("Error : " + str(i))
        

for i in input_keycode:
    print(chr(i), end ='')
