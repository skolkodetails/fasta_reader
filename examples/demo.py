from fasta_reader import FastaReader
import sys
import os
def main():
    reader = FastaReader(r'C:\Users\veram\OneDrive\Documents\labs\fasta_reader_lab13\examples\gene.fna')
    if not reader.check():
        return
    for seq in reader.read():
        print(f'title: {seq.inf}')
        print(f'seq: {seq}')
        print(f'length: {len(seq)}')
        print(f'type: {seq.alph()}')

main()