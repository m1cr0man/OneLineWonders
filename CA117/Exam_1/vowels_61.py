print('\n'.join([w for R in __import__("sys").stdin for w,l in[(R.strip(),R.strip().lower())]if[c for c in l if c in"aeiou"]==list("aeiou")]))
