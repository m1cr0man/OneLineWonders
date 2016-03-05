_=[(lambda e,w:len([l for l in w if len(e)and l==e[0]and w.count(l)==1and not e.remove(l)])==4and not print(W,end=''))(list("evil"),W.lower())for W in __import__("sys").stdin]
