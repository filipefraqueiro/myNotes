import hmac
import base64
import time

# otpauth://totp/[LABEL]?secret=[SECRET]&issuer=[ISSUER]&algorithm=SHA1&digits=6&period=30
# secret is BASE32
# make a qrcode of the above
#
#
#
def int_to_bytestring(i, padding=8):
    """
    Turns an integer to the OATH specified
    bytestring, which is fed to the HMAC
    along with the secret
    """
    result = bytearray()
    while i != 0:
        result.append(i & 0xFF)
        i >>= 8
    # It's necessary to convert the final result from bytearray to bytes
    # because the hmac functions in python 2.6 and 3.3 don't work with
    # bytearray
    result = bytes(bytearray(reversed(result)).rjust(padding, b'\0'))
    # print(result)
    return result
#
#
#
def totp(key):
    time_ = time.time()
    time_ = time_/30
    time_ = int(time_)
    # print(time_)
    time_ = int_to_bytestring(time_)

    key = key.encode()
    key = base64.b32decode(key)

    res = hmac.digest(key, time_, "sha1")
    # print(res)

    digits = 6
    offset = res[-1] & 0xf
    code = ((res[offset] & 0x7f) << 24 |
            (res[offset + 1] & 0xff) << 16 |
            (res[offset + 2] & 0xff) << 8 |
            (res[offset + 3] & 0xff))
    str_code = str(code % 10 ** digits)
    while len(str_code) < digits:
        str_code = '0' + str_code

    print(str_code)
    return str_code
#
#
#
if __name__ == "__main__":
    key = "".upper()
    totp(key)
#
#
#