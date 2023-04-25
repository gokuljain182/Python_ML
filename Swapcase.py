def swapi(string):
    k = ''
    for i in string:
        if i.islower():
            k += i.upper()
        else:
            k += i.lower()
    return k


name = input("Enter string")
ret = swapi(name)
print(ret)
