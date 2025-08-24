data = b'\xAF\x85\xDE\xBA\x7E\x78\x47\x5C\x97\xE2\xA0\xC5\x62\x1C\x3A\x30' \
       b'\x9C\xFE\xA3\xC5\x71\x67\x47\x36\x84\x9F\xDE\xCA\x1E\x79\x21\x34' \
       b'\x85\xE3\xC5\xE3'

stack = []
param = 0x63431577
for i in range(0, len(data) - 1, 4):
	chunk = int.from_bytes(data[i:i+4], 'big')
	stack.append(chunk ^ int(param) ^ 0xaaaaaaaa)
	param = chunk

print(stack)
byte_data = b''.join([i.to_bytes(4, byteorder='big') for i in stack])

print(byte_data)

bytes_list = [
    0x48, 0x79, 0x00, 0x00, 0x0e, 0x7a, 0x48, 0x78,
    0x00, 0x01, 0x48, 0x78, 0x00, 0x0f, 0x4e, 0xb9,
    0x00, 0x00, 0x07, 0xf2, 0x4f, 0xef, 0x00, 0x0c,
    0x48, 0x79, 0x00, 0x00, 0x0e, 0x83, 0x48, 0x78
]

local_4 = 0
for b in reversed(bytes_list):
	local_4 = int(b) + local_4 * 2
print(param)
print(local_4)
print(hex(local_4))
