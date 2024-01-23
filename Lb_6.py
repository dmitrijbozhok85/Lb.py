def scanner(qr_code):
    def traverse_qr():
        pos_x, pos_y, dir = 20, 20, -1
        while True:
            for i in range(2):
                yield qr_code[pos_x][pos_y - i] ^ ((pos_x + pos_y - i) % 2 == 0)
            pos_x += dir
            if pos_x == 8 or pos_x > 20:
                dir *= -1
                pos_x += dir
                pos_y -= 2

    qr_traversal = traverse_qr()
    bits = [next(qr_traversal) for _ in range(76)]
    bits_str = ''.join(map(str, bits))
    msg_length = int(bits_str[4:12], 2)
    decoded_msg = "".join(chr(int(bits_str[i:i+8], 2)) for i in range(12, msg_length * 8 + 12, 8))

    return decoded_msg
