
def ROL(data, shift):
    for i in range(shift):
        p = data//(0x100 >> 1)
        data = p+((data<<1)&0xff)
    return data

key_byte = [0x77 ,0xAD ,0x07 ,0x02 ,0xA5 ,0x00, 0x29 ,0x99]
MAX=20
flag = []
s = [0]

for j in range(0x30, 0x5B):
    s[0] = j
    i = 0
    for i in range(10):
        k = key_byte[i%7] ^ ROL(s[i],s[i]&7)
        '''if (not k):
            flag.append(s)
            break'''
        s.append(k)
    flag.append(s)
    j +=1
    s =[0]

for j in flag:
    res = ""
    for i in j:
        res+=chr(i)
    print res

