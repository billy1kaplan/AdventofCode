# Day 5:
import hashlib


def find_password(door_id: str):
    password = ''
    digits = 0
    i = 0
    while digits < 8:
        hsh = hashlib.md5((door_id + str(i)).encode('utf-8')).hexdigest()
        if hsh[:5] == '00000':
            digits += 1
            password += hsh[5]
        i += 1
    return password


def find_password2(door_id: str):
    password = ['_']*8
    digits = 0
    i = 0
    while digits < 8:
        hsh = hashlib.md5((door_id + str(i)).encode('utf-8')).hexdigest()
        if hsh[:5] == '00000':
            try:
                idx = int(hsh[5])
                if idx < 8 and password[idx] == '_':
                    password[idx] = hsh[6]
                    print('DECRYPTING:', ''.join(password))
                    digits += 1

            except ValueError:
                pass
        i += 1
    return password


if __name__ == '__main__':
    assert find_password('abc') == '18f47a30'
    print('Password:', find_password('ugkcyxxp'))
    find_password2('ugkcyxxp')
