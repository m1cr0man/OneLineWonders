(lambda W:[print("%s : %d"%(w,W.count(w)))for w in sorted(set(W))if len(w)>3 and W.count(w)>=3])([w.strip("!&'(),-.:;?_").lower()for l in __import__('sys').stdin for w in l.split()])
