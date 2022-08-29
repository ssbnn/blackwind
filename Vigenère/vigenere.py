mes = 'attack at dawn'
key = 'lemon'
code = 'lxfopv mh oeib'

def encryption(mes, key):
    y = 0
    debug = []
    for x in range(len(mes)):
        if mes[x] == ' ':
            debug.append(' ')
        else:
            debuged = chr((((ord(mes[x]))%97 + (ord(key[y]))%97)%26)+97)
            debug.append(debuged)
        if y < len(key)-1:
            y += 1
        else:
            y = 0
    return ''.join(debug)

def decryption(code, key):
    y = 0
    debug = []
    for x in range(len(code)):
        if code[x] == ' ':
            debug.append(' ')
        else:
            debuged = chr((((ord(code[x]))%97+26 - (ord(key[y]))%97)%26)+97)
            debug.append(debuged)
        if y < len(key)-1:
            y += 1
        else:
            y = 0
    return ''.join(debug)

print(encryption(mes, key))
print(decryption(code, key))