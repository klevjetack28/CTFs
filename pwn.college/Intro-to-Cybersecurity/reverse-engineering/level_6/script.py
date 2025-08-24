byte_value = 0x20
repeat_count = 0x66d

with open('output.cimg', 'wb') as file:
    file.write(bytes([0x63, 0x49, 0x4d, 0x47, 0x01, 0x00, 0x50, 0x18]))
    for _ in range(repeat_count):
        file.write(bytes([byte_value]))

    byte_value = 0x55
    repeat_count = 0x113
    for _ in range(repeat_count):
        file.write(bytes([byte_value]))

