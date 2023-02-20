def SearchName(arr,name):

    for i in arr:
        if i == name:
            return 1
    return 0

arr = ["coder","codex","mypc","AI"]
print(SearchName(arr,name="codexr"))