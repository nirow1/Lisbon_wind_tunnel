import numpy as np
import struct

def on_off_bit(i :int, current_byte: bytearray):
    logo_byte = current_byte
    byte_index = (i - 1) // 8
    bit_index = (i - 1) % 8
    logo_byte[byte_index] ^= (1<< bit_index)
    return logo_byte


def dict_to_bytearray(dictionary) -> bytearray:
    bits = np.array([int(dictionary[i]) for i in range(1, len(dictionary) + 1)])
    chunks = np.split(bits, len(bits) // 8)
    bytes_list = [np.packbits(chunk[::-1])[0] for chunk in chunks]
    return bytearray(bytes_list)

def add_sec_to_current_time(seconds: int):
    from datetime import datetime, timedelta
    current_time = datetime.now()
    new_time = current_time + timedelta(seconds=seconds)
    return new_time

def combine_to_float( float_list ):
    # Combine the high and low 16-bit numbers into a 32-bit integer
    combined = (float_list[0] << 16) | float_list[1]

    # Convert the 32-bit integer to a float
    float_value = struct.unpack('!f', struct.pack('!I', combined))[0]

    return float_value
