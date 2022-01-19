str='label'
new=''

for c in str:
	new=new+chr(ord(c)^13)
print(new)