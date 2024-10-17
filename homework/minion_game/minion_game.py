def minion_game(s: str) -> str:
    countK=0
    countS=0
    maganh="AEIOU"
    hossz=len(s)
    substringek=[]
    for i in range(hossz):
        substringek.append(s[i])
    for x in range(2, hossz+1):
        for start in range(hossz-x+1):
            substringek.append(s[start:start+x])

    for j in substringek:
        elso=j[0].upper()
        if elso in maganh:
            countK=countK+1
        else:
            countS=countS+1
    if countK>countS:
        return f"Kevin {countK}"
    elif countS>countK:
        return f"Stuart {countS}"
    else:
        return "Draw"