import gzip

ts = 0
tv = 0
pu = {"A", "G"}
py = {"C", "T"}

with gzip.open("sample.ann.vcf.gz", "rt") as handle:
    for line in handle:
        if line.startswith("##"):
            continue

        if line.startswith("#"):
            header = line.split("\t")
            ref_idx = header.index("REF")
            alt_idx = header.index("ALT")
            continue

        row = line.split("\t")
        ref = row[ref_idx]
        alt = row[alt_idx]

        if ref in pu and alt in py:
            ts += 1
        elif ref in py and alt in py:
            ts += 1
        elif ref in pu and alt in pu:
            tv += 1
        elif ref in pu and alt in py:
            tv += 1

print(round(ts / tv, 4))
