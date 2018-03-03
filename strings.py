him = "bobby"
#ex 1
print(him.upper())
#ex 2
print(him.capitalize())
#ex 3
print(him[::-1])

#ex 4
pGraph = "geologist"
pGraph = pGraph.upper()
pGraph = pGraph.replace('A', '4')
pGraph = pGraph.replace('E', '3')
pGraph = pGraph.replace('G', '6')
pGraph = pGraph.replace('I', '1')
pGraph = pGraph.replace('O', '0')
pGraph = pGraph.replace('S', '5')
pGraph = pGraph.replace('T', '7')
print(pGraph)

#ex 5
word = "heel moo man"
word = word.replace('ee','eeeeeee')
word = word.replace('oo','ooooooo')
print(word)

#ex 6
alphabet = 'abcdefghijklmnopqrstuvwxyz'
#print(alphabet[5])
phrase = "lbh zhfg hayrnea jung lbh unir yrnearq"
shift = 13
result = ''

for char in phrase:
    if char not in alphabet:
        new_char = char
    else:
        idx = alphabet.find(char)
        new_idx = (idx + shift) % 26
        new_char = alphabet[new_idx]
    result += new_char

print(result)