(lambda W:[print("%s : %d"%(w,W.count(w)))for w in sorted(set(W))])([w.strip("!&'(),-.:;?_").lower()for l in __import__('sys').stdin for w in l.split()])
