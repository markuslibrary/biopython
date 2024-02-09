import wget
from Bio import SeqIO
import gzip 

path = "C:/Users/Claire/Documents/GitHub/biopython/workshop-1/sample-data/" # Change this to the path of your sample-data folder

# Uncomment the line below to download the large data file. Re-comment once it is downloaded
# wget.download("http://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/xenoMrna.fa.gz", out=path)

count = 0

with gzip.open(path + "xenoMrna.fa.gz", "rt") as input_handle:
    with open(path + "xenoMrna_short.fa", "w") as output_handle:
        with gzip.open(path + "xenoMrna_short.fa.gz", "wt") as output_handle_gz:
            seq_iter = iter(SeqIO.parse(input_handle, "fasta"))
            while count < 500000:
                seq = next(seq_iter)
                SeqIO.write(seq, output_handle, "fasta") # Write record in gb format to the new data file
                SeqIO.write(seq, output_handle_gz, "fasta") # Write record in gb format to the new data file
                count += 1

print(count) # You should see 500000          
print("I am done")

