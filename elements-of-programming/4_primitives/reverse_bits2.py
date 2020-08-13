PRECOMPUTED = {}

def swap_bits(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x


def reverse_bits(x, msb):
    for i in range(msb // 2 + 1):
        # print('i: {}, msb-i: {}, msb//2: {}, {:b}'.format(i, msb-i, msb//2, x))
        x = swap_bits(x, i, msb - i)
    return x


def pre_compute(msb):
    for i in range(0x10000):
        PRECOMPUTED[i] = reverse_bits(i, msb)


def reverse_word(x):
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    return (PRECOMPUTED[x & BIT_MASK] << (3 * MASK_SIZE) |
            PRECOMPUTED[(x >> MASK_SIZE) & BIT_MASK] << (2 * MASK_SIZE) |
            PRECOMPUTED[(x >> (2 * MASK_SIZE)) & BIT_MASK] << MASK_SIZE |
            PRECOMPUTED[(x >> (3 * MASK_SIZE)) & BIT_MASK])

if __name__ == '__main__':
    pre_compute(15)
    print('{:b}'.format(reverse_word(15)))
