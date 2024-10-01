
infile = open ("info_security-1.txt", "r")
contents = infile.read()
encrypted_dict = {
    'A': '9', 'B': '#', 'C': 'x', 'D': '4', 'E': '?', 'F': 'w', 
    'G': '5', 'H': 'q', 'I': '8', 'J': 'z', 'K': '%', 'L': '0', 
    'M': 'r','N': '1', 'O': 'v', 'P': '@', 'Q': 'n', 'R': '7', 
    'S': 'd', 'T': '*', 'U': 'e', 'V': '2', 'W': 'm', 'X': 'k', 
    'Y': '$', 'Z': 'j','a': 'b', 'b': '3', 'c': 'f', 'd': '6',
    'e': 'p', 'f': 'y', 'g': 'u', 'h': 'c', 'i': 's', 'j': 't', 
    'k': '&', 'l': 'o', 'm': 'h','n': 'a', 'o': 'l', 'p': 'i', 
    'q': 'g', 'r': '1', 's': 'r', 't': '0', 'u': '9', 'v': 'k', 
    'w': 'x', 'x': 'j', 'y': '4', 'z': '!'
}

outfile = open('encrypted.txt','w')

for l in contents:
    if l in encrypted_dict.keys():
        encrypted_let = encrypted_dict[l]
        outfile.write(encrypted_let)
    elif l == ' ':
        outfile.write(' ')
    elif l == '.':
        outfile.write('.')
    elif l == ':':
        outfile.write(':')
    else:
        pass

infile.close()