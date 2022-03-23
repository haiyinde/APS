# D2
import sys
sys.stdin = open("input.txt", "r")

import base64

T = int(input())
for t in range(1, T+1):
    encoded_str = input()
    str_bytes = base64.b64decode(encoded_str)
    decoded_str = str_bytes.decode('ascii')

    print("#{} {}".format(t, decoded_str))
