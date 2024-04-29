seq = ""
with open("test.fasta") as handle:
    for line in handle:
        if line.startswith(">"):
            continue

        seq += line.strip

print(len(seq))
print(seq.count("A"))
print(seq.count("C"))
print(seq.count("G"))
print(seq.count("T"))
