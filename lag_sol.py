#!/usr/bin/env pyhon3

def generate_key(password='password', key=0x9487):
    assert type(password) is str
    assert type(key) is int

    for p in password:
        key *= ord(p)
        key ^= ord(p)

    return key

def cipher(data, key):
    output = []

    for i in data:
        b = (i ^ key) & 0xff # data must be one byte after encryption
        key = (key * 0xc8763) + 9487
        output.append(b)

    return bytes(output)

def main():
    with open('dist/lag/enc', 'rb') as Flag:
        data = Flag.read()

    for key in range(256):
        dec = cipher(data, key)
        if dec.startswith(b'TDOH{') and dec.endswith(b'}\n'):
            print(dec)

if __name__ == '__main__':
    main()
