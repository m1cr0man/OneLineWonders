print(__import__("re").sub("([^aeiou]y|fe|ch|sh|[fxszo])$",lambda m:("v"if"f"in m.group(0)else m.group(0)[:-1]+"i"if"y"in m.group(0)else m.group(0))+"e",__import__("sys").argv[1])+"s")
