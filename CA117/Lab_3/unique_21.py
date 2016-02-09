print(len(set(__import__('re').findall(r"\w+",__import__('sys').stdin.read().lower()))))
