from count_variant import count_variant
from unittest import mock
import unittest


@mock.patch(
    "builtins.open",
    new_callable=mock.mock_open,
    read_data=(
        "##META\n"
        "#CHROM\tPOS\tID\tREF\tALT\n"
        "chr1\t100\t.\tA\tC\n"
        "chr1\t200\t.]tT\tG\n"
    ),
)
def test_count_variant(mock_open):
    res = count_variant("sample.vcf")
    assert res == {"deletion": 1, "insertion": 2, "snp": 2}
