import array

f = open("data","rb")
encrypted = bytearray(f.read())
f.close()

a = array.array('i',(i*4 for i in range(0,0xc4/4+1)))
for i in range(0,len(a)):
    encrypted[i] = encrypted[i]^a[i]

print("Flag :" + encrypted)
