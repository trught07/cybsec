def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])
    
key = byte_xor(b"sbi`d\x7fk h! O!%O}iOv$f eb!'#Ori'um"
,b"gggggggggg")
print(key)

#above code works perfectly
#s1 = "
#s2 = "a23"

#a_list = [chr(ord(a) ^ ord(b)) for a,b in zip(s1, s2)]
#print(a_list)