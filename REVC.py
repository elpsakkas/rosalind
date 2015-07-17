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
