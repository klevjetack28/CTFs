byte_value = 0x20
repeat_count = 0x780

with open('output.cimg', 'wb') as file:
    file.write(bytes([0x63, 0x49, 0x4d, 0x47, 0x02, 0x00, 0x50, 0x18]))
    for i in range(repeat_count):
            byte_value = 0x8c
            file.write(bytes([byte_value]))
            byte_value = 0x1d
            file.write(bytes([byte_value]))
            byte_value = 0x40
            file.write(bytes([byte_value]))
            byte_value = 0x55
            file.write(bytes([byte_value]))
