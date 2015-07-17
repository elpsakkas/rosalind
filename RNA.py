import string

dna=raw_input(" Please enter DNA sequence: ")

rna=string.replace(dna,'T', 'U')


text_file=open("RNA.txt", "w")
text_file.write("%s" % rna)






# solution 2 using the list data structure


dna= raw_input("Please enter DNA sequence: ")

for base in dna:
    if base=="T":
        print "U",
    else:
        print base,
        
