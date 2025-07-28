def encode(numbers: list[int]) -> list[int]:
    encoded: list[int] = []
    for number in numbers:
        if number == 0:
            encoded.append(0x00)
            continue

        bytes_list: list[int] = []
        while number > 0:
            bytes_list.insert(0, number & 0x7F)
            number >>= 7

        for i in range(len(bytes_list) - 1):
            bytes_list[i] |= 0x80  # set MSB to 1 except last

        encoded.extend(bytes_list)

    return encoded


def decode(bytes_: list[int]) -> list[int]:
    numbers: list[int] = []
    current = 0
    for byte in bytes_:
        current = (current << 7) | (byte & 0x7F)
        if (byte & 0x80) == 0:  # MSB is 0 → end of value
            numbers.append(current)
            current = 0

    if bytes_ and (bytes_[-1] & 0x80):
        raise ValueError("incomplete sequence")

    return numbers
