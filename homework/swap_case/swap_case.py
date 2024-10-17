def swap_case(s: str) -> int:
    x= ""
    for karakter in s:
        if karakter.islower():
            x += karakter.upper()
        elif karakter.isupper():
            x += karakter.lower()
        else :
            x+= karakter
    return x
