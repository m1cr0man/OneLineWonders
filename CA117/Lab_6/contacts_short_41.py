(lambda a:[(lambda a,n:print("Phone: "+a[n]if n in a else "No such contact"))(a,n.strip())for n in __import__('sys').stdin])({n:p for l in open(__import__('sys').argv[1],'r')for n,p in[l.split()]})
