def rle_encode(data):
    """
    Encodes a string using Run-Length Encoding (RLE).

    Args:
        data (str): The input string to be encoded.

    Returns:
        str: The RLE encoded string.
    """
    if not data:
        return ""

    encoded = []
    count = 1
    prev_char = data[0]

    for char in data[1:]:
        if char == prev_char:
            count += 1
        else:
            if count > 1:
                encoded.append(str(count))
            encoded.append(prev_char)
            count = 1
            prev_char = char

    if count > 1:
        encoded.append(str(count))
    encoded.append(prev_char)

    return "".join(encoded)

def rle_decode(data):
    """
    Decodes a Run-Length Encoded (RLE) string.

    Args:
        data (str): The RLE encoded string to be decoded.

    Returns:
        str: The decoded original string.
    """
    if not data:
        return ""

    decoded = []
    i = 0
    n = len(data)

    while i < n:
        if data[i].isdigit():
            num_str = []
            while i < n and data[i].isdigit():
                num_str.append(data[i])
                i += 1
            count = int("".join(num_str))

            if i < n:
                char = data[i]
                decoded.append(char * count)
                i += 1
        else:
            decoded.append(data[i])
            i += 1

    return "".join(decoded)

original = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
encoded = rle_encode(original)
decoded = rle_decode(encoded)

print(f"Original: {original}")
print(f"Encoded: {encoded}")
print(f"Decoded: {decoded}")
print(f"Original == Decoded: {original == decoded}")