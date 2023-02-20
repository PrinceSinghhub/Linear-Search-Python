def SearchChar(string,c):

    for i in string:
        if i == c:
            return f"Char are Found!"
    return f"Char are not Found!"

name = "codex coder"
check = "f"
print(SearchChar(name,check))