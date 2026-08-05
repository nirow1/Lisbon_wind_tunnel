from datetime import datetime
from typing import Sequence


def list_to_short(bits: Sequence[int], msb_first: bool = True, signed=False) -> int:
    """Convert a sequence of 16 bits (0/1) to a signed or unsigned short (0..65535 or -32768..32767).

    Args:
        bits: Sequence with exactly 16 values, each 0 or 1.
        msb_first: If True, bits[0] is MSB. If False, bits[0] is LSB.
        signed: If True, return a signed 16-bit integer (-32768..32767).
                If False, return an unsigned 16-bit integer (0..65535).

    Returns:
        Signed or unsigned short value in range -32768..32767 or 0..65535.

    Raises:
        TypeError: If bits is not a sequence.
        ValueError: If length is not 16 or values are not 0/1.
    """
    if not isinstance(bits, Sequence):
        raise TypeError("bits must be a sequence of 16 items")

    if len(bits) != 16:
        raise ValueError("bits must contain exactly 16 values")

    if any(bit not in (0, 1) for bit in bits):
        raise ValueError("each bit must be 0 or 1")

    value = 0
    if msb_first:
        for bit in bits:
            value = (value << 1) | bit
    else:
        for shift, bit in enumerate(bits):
            value |= (bit << shift)

    if signed:
        if value & 0x8000:  # if MSB is 1 → negative number
            value -= 0x10000  # convert to signed range

    return value


def control_dict_to_bytes(ctrl: dict, endian="little") -> bytearray:
    # Map keys to bit positions
    bit_map = {
        "start": 0, "stop": 1, "ack": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
        "8": 8, "PID": 9, "10": 10, "11": 11, "12": 12, "13": 13, "14": 14, "15": 15
    }

    value = 0

    # Build the 16-bit word
    for key, bit in bit_map.items():
        if ctrl.get(key, 0):
            value |= (1 << bit)

    # Convert to two bytes
    if endian == "little":
        return bytearray([value & 0xFF, (value >> 8) & 0xFF])
    else:  # big endian
        return bytearray([(value >> 8) & 0xFF, value & 0xFF])


def byte_to_bits(byte, endian="little"):
    bits = [(byte >> i) & 1 for i in range(0, 16)]

    if endian == "big":
        return list(reversed(bits))

    return bits
