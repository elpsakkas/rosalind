'''The dna sequence is initially reversed and then it saved in a new list
   under dna1; the program checks every base and substitutes with the
   complementary base '''
   
dna= raw_input("Please enter DNA sequence: ")
dna=dna.upper()
dna1=dna[::-1]
new=[]
for base in range(len(dna1)):
    if dna1[base]=="A":
        new.append("T")
        continue
    elif dna1[base]=="C":
        new.append("G")
        continue
    elif dna1[base]=="G":
        new.append("C")
        continue
    elif dna1[base]=="T":
        new.append("A")
        continue
    else:
        print "Your sequence contains strange characters"
        break
print "".join(new)

# Second solution using dictionaries structure

base_compl={'A':'T', 'C':'G','G':'C', 'T':'A','N':'N'}
seq=list(raw_input("Please enter DNA sequence:"))
seq1=seq[::-1]
new=[]
for i in seq1:
    for key in base_compl:
        if i==key:
            new.append(base_compl[key])
            continue
print ''.join(new)
