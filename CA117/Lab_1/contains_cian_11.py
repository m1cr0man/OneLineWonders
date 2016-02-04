print(all((lambda x:[x[1].count(s)<=x[2].count(s)for s in x[1]])(__import__('sys').argv)))
