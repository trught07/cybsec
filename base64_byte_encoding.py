import base64
byte=b'\x12$Y\x08\x05$$/\x02\n\x1ee),\x04%\x1fbl!%=s0r \x1b\x1brl\x04#\x14_}J'




base=base64.b64encode(byte)
print(base)

#ALternate code from Internet

#import base64
#from binascii import unhexlify

#hex = unhexlify('')
#flag = base64.b64encode(hex)
#print(flag)