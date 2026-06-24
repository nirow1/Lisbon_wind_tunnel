from typing import Sequence


def list_to_ushort(bits: Sequence[int], msb_first: bool = True) -> int:
    """Convert a sequence of 16 bits (0/1) to an unsigned short (0..65535).

    Args:
        bits: Sequence with exactly 16 values, each 0 or 1.
        msb_first: If True, bits[0] is MSB. If False, bits[0] is LSB.

    Returns:
        Unsigned short value in range 0..65535.

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

    return value


def byte_to_bits(byte):
    return [(byte >> i) & 1 for i in range(0, 16)]
