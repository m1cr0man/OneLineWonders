print(("Multiples of {}: {}\n"*6).format("3",[n for n in range(1,31)if not n%3],"3 squared",[n**2for n in range(1,31)if not n%3],"4 doubled",[n*2for n in range(1,31)if not n%4],"3 or 4",[n for n in range(1,31)if not(n%4and n%3)],"3 and 4",[n for n in range(1,31)if not(n%4or n%3)],"3 replaced",[n%3and n or'X'for n in range(1,31)]).strip())
