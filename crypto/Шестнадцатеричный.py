import pwn
print(bytes.fromhex('ed66878c338e662d3473f0d98eedbd0d'))
print(bytes.fromhex('7ae18c704272532658c10b5faad06d74'))
print(pwn.xor("z\xe1\x8cpBrS&X\xc1\x0b_\xaa\xd0mt\xedf\x87\x8c3\x8ef-4s\xf0\xd9\x8e\xed\xbd\r", 3))
print(pwn.xor("z\xe1\x8cpBrS&X\xc1\x0b_\xaa\xd0mt", 3))

# for i in range(1, 10000000):
#     b = pwn.xor("\xedf\x87\x8c3\x8ef-4s\xf0\xd9\x8e\xed\xbd\r", i)
#     if 'crypto' in str(b):
#         print(b, i)
#         break