decryted = [0x4D, 0x5A, 0x90, 0x00, 0x03, 0x00 \
            ,0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0xFF, 0xFF, 0x00, 0x00, 0xB8, 0x00, 0x00 \
            ,0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 \
            ,0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 \
            ,0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 \
            ,0x00, 0x00, 0xF0, 0x00, 0x00, 0x00]

encryted = [0xDE, 0xC0, 0x1B, 0x8C, 0x8C, 0x93, 0x9E, 0x86, 0x98, 0x97, 0x9A, 0x8C\
            ,0x73, 0x6C, 0x9A, 0x8B, 0x34, 0x8F, 0x93, 0x9E, 0x86, 0x9C, 0x97, 0x9A, 0xCC\
            ,0x8C, 0x93, 0x9A, 0x8B, 0x8C, 0x8F, 0x93, 0x9E, 0x86, 0x9C, 0x97, 0x9A, 0x8C, 0x8C\
            ,0x93, 0x9A, 0x8B, 0x8C, 0x8F, 0x93, 0x9E, 0x86, 0x9C, 0x97, 0x9A, 0x8C, 0x8C, 0x93\
            , 0x9A, 0x8B, 0x8C, 0x8F, 0x93, 0x9E, 0x86, 0x6C, 0x97, 0x9A, 0x8C]

for i in range(len(encryted)):
    key_temp = encryted[i] ^ 0xFF
    key = key_temp ^ decryted[i]
    print(key)
