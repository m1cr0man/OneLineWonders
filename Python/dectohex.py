print("#"+''.join(["{:0>2}".format(hex(int(a))[2:])for a in __import__('sys').argv[1:]]))
