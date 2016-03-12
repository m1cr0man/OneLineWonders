print((lambda W:''.join([W[i+1]+W[i]for i in range(0,len(W)-1,2)])+(W[-1]if len(W)%2else''))(list(__import__("sys").argv[1])))
