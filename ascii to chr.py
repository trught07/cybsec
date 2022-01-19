ords = [97,108,111,104,97]
flag=''

print("Here is your flag:")

for i in ords:
	flag+=chr(i)
print(flag)

#print("".join(chr(o) for o in ords)) #if you wanna join characters
