import os
import sys
from Bio import SeqIO


def count_base_from_fasta(file_path):
    if not os.path.isfile(file_path):
        print(" # ERROR : file does not esits.")
        sys.exit()

    record = SeqIO.read(file_path, "fasta")
    data = dict()
    for base in record.seq:
        if base not in data:
            data[base] = 0
        data[base] += 1

    return data
