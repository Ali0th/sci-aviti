import gzip
from Bio.Seq import Seq
from tqdm import tqdm
import argparse
import os

def reverse_complement_p5(header):
    try:
        i7, i5 = header.strip().split(":")[-1].split("+")
        i5_rc = str(Seq(i5).reverse_complement())
        return header.replace(i5, i5_rc)
    except Exception:
        return header  # if malformed, skip modification

def process_fastq(in_path, out_path):
    # Estimate line count for progress bar (4 lines per record)
    with gzip.open(in_path, 'rt') as f:
        total_lines = sum(1 for _ in f)

    with gzip.open(in_path, 'rt') as fin, gzip.open(out_path, 'wt') as fout, tqdm(total=total_lines, desc=os.path.basename(in_path)) as pbar:
        while True:
            header = fin.readline()
            if not header:
                break  # EOF
            seq = fin.readline()
            plus = fin.readline()
            qual = fin.readline()

            if header.startswith("@"):
                header = reverse_complement_p5(header)

            fout.write(header)
            fout.write(seq)
            fout.write(plus)
            fout.write(qual)

            pbar.update(4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reverse complement AVITI p5 barcodes in FASTQ headers.")
    parser.add_argument("input_fastq", help="Path to input .fastq.gz file")
    parser.add_argument("output_fastq", help="Path to output .fastq.gz file with fixed headers")
    args = parser.parse_args()

    process_fastq(args.input_fastq, args.output_fastq)
