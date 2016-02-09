(lambda s:print(s==s[::-1]))(__import__('re').sub(r"\W","",__import__('sys').argv[1].lower()))
