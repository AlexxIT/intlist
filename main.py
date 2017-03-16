def test(layers):
    import intlist

    a = ','.join([str(y) for y in layers])
    b = intlist.encode(layers)
    c = intlist.encode_diff(layers)

    print len(a), a
    print len(b), b
    print len(c), c
    print

    assert set(layers) == set(intlist.decode_diff(c))


test([1, 3, 5, 31, 32, 33, 40, 80, 130, 200])
test([9108, 14092, 14090, 14093, 14094, 14091, 14095, 14100, 14044, 9212, 13928, 13929, 13932, 13935, 13933, 13936, 13939, 13940, 13988, 9019, 9160, 9161, 13974])
test([784, 785, 782, 638, 786, 787])
