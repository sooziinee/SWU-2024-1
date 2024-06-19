from unittest.mock import patch
from read_fasta import count_base_from_fasta

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from read_fasta import count_base_from_fasta


@patch("os.path.isfile")
@patch("read_fasta.SeqIO.read")
def test_count_base_from_fasta(mock_seqio_read, mock_isfile):
    mock_isfile.return_value = True
    mock_seqio_read.return_value = SeqRecord(Seq("AAC"))
    exp = {"A": 2, "C": 1}
    assert count_base_from_fasta("file.fasta") == exp
    mock_seqio_read.assert_called_once_with("file.fasta", "fasta")
