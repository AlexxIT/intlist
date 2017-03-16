# encoding: utf-8

MAP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
MAP0 = [0, 0x20, 0x30, 0x38]


def encode(items):
    """
    Кодирование массива integer для передачи в качества GET-параметра.

    Коридование по аналогии с UTF-8: https://ru.wikipedia.org/wiki/UTF-8

    Используется алфавит URI Unreserved Characters - 64 символа, позволяющих
    закодировать по 6 байт: https://en.wikipedia.org/wiki/Percent-encoding

    #  Байт  Бит  Шаблон полностью
    #  1     5    --0xxxxx
    #  2     10   --10xxxx --xxxxxx
    #  3     15   --110xxx --xxxxxx --xxxxxx
    #  4     20   --1110xx --xxxxxx --xxxxxx --xxxxxx

    """

    result = ''

    for x in items:
        s = ''
        while True:
            if x > 0x1F:
                s = MAP[x & 0x3F] + s
                x >>= 6
            else:
                s = MAP[x | MAP0[len(s)]] + s
                break
        result += s

    return result


def encode_diff(items):
    """
    Аналогичен encode, но сохраняет смещение значения от предыдущего. Применимо
    когда порядок элементов не имеет значения.

    """

    result = ''

    items.sort()
    x0 = 0

    for x in items:
        dx = x - x0
        x0 = x

        s = ''
        while True:
            if dx > 0x1F:
                s = MAP[dx & 0x3F] + s
                dx >>= 6
            else:
                s = MAP[dx | MAP0[len(s)]] + s
                break
        result += s

    return result


def decode_diff(string):
    result = []

    i = 0

    x0 = 0

    while i < len(string):
        x = MAP.index(string[i])
        i += 1

        if x >= 0x38:
            x &= 0x03
            n = 3
        elif x >= 0x30:
            x &= 0x07
            n = 2
        elif x >= 0x20:
            x &= 0x0F
            n = 1
        else:
            n = 0

        for j in range(n):
            x <<= 6
            x |= MAP.index(string[i])
            i += 1

        x0 += x

        result.append(x0)

    return result
