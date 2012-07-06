import Image
from xml.etree.ElementTree import ElementTree
import unittest

def isolate(n,x):
    return ( x & ( 0b11 << (2 * n) ) ) >> (2 * n)


def load_cip(tree):
    width = int(tree.findtext(".//Width"))
    height = int(tree.findtext(".//Height"))
    depth = int(tree.findtext(".//Depth"))
    data = tree.findtext(".//Data")

    MAX_LUM = 255
    MAX_VAL = (1 << depth) - 1
    COLOR_SCALE = MAX_LUM / MAX_VAL
    FLIP_SIZE = 4

    assert width % 4 == 0


    field = width * height

    idata = int(data, 16)

    print len(data) * 2

    elst = [isolate(i, int(x, 16)) for x in data for i in [1, 0]]
    padding_len = field - len(elst)
    padding = [0 for i in range(padding_len)]
    elst = padding + elst
    #elst2 = [(idata & (MAX_VAL << i * 2)) >> i * 2 for i in range(field)][::-1]
    
    clst = [(MAX_LUM - e * COLOR_SCALE) for e in elst]
    flipped_values = [clst[i*FLIP_SIZE:i*FLIP_SIZE+FLIP_SIZE][::-1] for i in range(field / FLIP_SIZE)]

    l = []
    for fl_val in flipped_values:
        l.extend(fl_val)

    im = Image.new('L', (width, height))
    im.putdata(l)
    return im

def pack(x1, x2):
    return (x1 << 2) + x2

def dump_cip(im):
    depth = 2

    MAX_LUM = 255
    MAX_VAL = (1 << depth) - 1
    COLOR_SCALE = (MAX_LUM+1) / (MAX_VAL+1)
    FLIP_SIZE = 4


    l = list(im.getdata())

    width, height = im.size

    assert width % 4 == 0

    field = width * height

    flipped_values = [l[i*FLIP_SIZE:i*FLIP_SIZE+FLIP_SIZE][::-1] for i in range(field / FLIP_SIZE)]    

    flipped_list = []
    for fl_val in flipped_values:
        flipped_list.extend(fl_val)

    #flipped_values = sum(flipped_values, [])

    print MAX_LUM, COLOR_SCALE

    elst = [int(round((MAX_LUM + 1 - e) / float(COLOR_SCALE))) - 1 for e in flipped_list]

    # print zip([(MAX_LUM + 1 - e) / float(COLOR_SCALE) - 1 for e in flipped_list], flipped_list)

    #idata = reduce(lambda c, (i, x): c + (x << i * 2), enumerate(reversed(elst)), 0)

    # print flipped_values
    # print elst
    # print idata

    hex_vals = ['%X' % pack(elst[i*2], elst[i*2+1]) for i in range(len(elst)/2)]

    data = ''.join(hex_vals)

    return data

def test():
    width, height = 4, 1
    im = Image.new('L', (width, height))
    l = [0, 85, 170, 255]
    im.putdata(l)
    data = dump_cip(im)
    exp_data = '%X' % (0b00011011)
    assert exp_data == data, (bin(int(exp_data, 16)), bin(int(data, 16)))
    

if __name__ == '__main__':
    import sys

    fname = sys.argv[1]
    f = open(fname)

    tree = ElementTree()
    tree.parse(f)

    im = load_cip(tree)
    im.show()
