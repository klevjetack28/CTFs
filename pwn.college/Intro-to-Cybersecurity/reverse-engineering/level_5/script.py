byte_value = 0x30
repeat_count = 0x780

with open('output.cimg', 'wb') as file:
    file.write(bytes([0x63, 0x49, 0x4d, 0x47, 0x01, 0x00, 0x50, 0x18]))
    for _ in range(repeat_count):
        file.write(bytes([byte_value]))

