(lambda l:print(''.join([l[i+1]+l[i]for i in range(0,len(l)-1,2)])+(l[-1]if len(l)%2else'')))(list(__import__("sys").argv[1]))
