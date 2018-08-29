import base64

a = [16, 17, 33,51, 68, 102, 51, 160, 144, 181, 238, 17]
b = [74, 87, 77, 70, 29, 49, 117, 238, 241, 226, 163, 44]

flag = ''

for i in range(0,12):
    flag += chr(a[i]^b[i])
print(flag)
print(base64.b64decode(flag))
