import gzip

result = 0
with gzip.open("sample.ann.vcf.gz", "rt") as handle:
    for line in handle:
        if line.startwith("#"):
            continue

        result += 1

print(result)
