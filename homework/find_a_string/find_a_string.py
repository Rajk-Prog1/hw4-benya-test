def find_a_string(original_str: str, substr: str) -> int:
    count=0
    if substr == "":
        return 0
    for i in range(len(original_str)):
        teszt=original_str[i:i+len(substr)]
        if teszt==substr:
            count=count+1
    return count

print(find_a_string("abc", ""))
