

def bin2str(inp):
    num = int(inp, 2)
    try:
        s = num.to_bytes((num.bit_length() + 7) // 8, 'big').decode()
    except UnicodeDecodeError:
        s = "Invalid Input"
    return s


def str2bin(s):
    return bin(int.from_bytes(s.encode(), byteorder="big"))[2:]
