# This script uses the GMOD launch option "-condebug" to write your console to a file
# With this file we can read the text chat and decode the NPST Boss Keypad so you don't have to spend time decoding it in the room

import pyperclip
seek = 0
ingamename = "REPLACE NAME HERE:" # leave the : at the end of your name, this directly reads the ingame chat, format is "name:"
path = "C:/Program Files (x86)/Steam/steamapps/common/GarrysMod/garrysmod/console.log" # replace this with the path to your console.log file, by default it will be here 

def decode(codeinput, npstcode):
    return ' '.join([npstcode.get(char, char) for char in codeinput])

npstcode = {'a': '74','b': '75','c': '76','d': '77','e': '78','f': '79','g': '80','h': '81','i': '82','j': '83','k': '84','l': '85','m': '86','n': '87','o': '88','p': '89','q': '90','r': '91','s': '92','t': '93','u': '94','v': '95','w': '96','x': '97','y': '98','z': '99'}
# clear the console.log folder when you start the script to limit how large the file gets, it can get seriously big if left untouched
with open(path, "w", encoding='UTF-8'):
    pass 

while True:
    with open(path, "r", encoding='UTF-8') as f:
        f.seek(seek)
        for line in f:
            if ingamename in line:
                start_index = line.find(ingamename) + len(ingamename)
                checkline = line[start_index:].strip()
                lowercase_checkline = "".join(char for char in checkline if char.islower())
                if 0 < len(lowercase_checkline) <= 4: # check if the text you typed in chat is 3-4 characters, this is what the code is, it will automatically assume all 3-4 char lowercase messages are the code and decode them
                    codeinput = checkline
                    codeoutput = decode(codeinput, npstcode)
                    print("Code Input:", codeinput)
                    print("Code Output:", codeoutput)
                    pyperclip.copy(codeoutput) # Copy keypad code to your clipboard
        seek = f.tell()