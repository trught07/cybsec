import base64
hex_enc=input("")
byte = bytes.fromhex(hex_enc)
print(byte)
b64_encoded_string = base64.b64encode(byte)
str=b64_encoded_string.decode()
print(str)