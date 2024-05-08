import gzip

gt_count = dict()

with gzip.open("sample.ann.vcf.gz", "rt") as handle:
    for line in handle:
        if line.startswith("#"):
            continue

        row = line.strip().split("\t")
        gt = row[-1].split(":")[0].replace("|", "/")
        if gt not in gt_count:
            gt_count[gt] = 0

        gt_count[gt] += 1

print(gt_count)
