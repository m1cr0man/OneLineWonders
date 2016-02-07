(lambda p,s:print((p.lower()!=p)+(p.upper()!=p)+([]!=s("[0-9]",p))+([]!=s("[^0-9A-Za-z]",p))))(__import__("sys").argv[1],__import__('re').findall)
