
infile = open("sometext-1.txt","r")
text = infile.read()
words = text.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
for words,count in word_count.items(): 
    f"{words}:{count}"

print(word_count)

infile.close()