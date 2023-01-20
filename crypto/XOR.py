import pwn
a = 'label'
b = pwn.xor('crypto', 13)
print(b)