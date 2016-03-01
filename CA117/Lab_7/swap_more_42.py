swap_unique_keys_values=lambda d:{v:k for k,v in d.items()if list(d.values()).count(v)==1}
