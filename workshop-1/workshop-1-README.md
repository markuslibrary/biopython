# Workshop 1: Sequence Data and SeqIO

The contents of this jupyter notebook are preceded by:

1. An overview of sequence data
2. Instructions for a recommended installation of Python/Biopython using miniconda, as well as the importance of managing Python environments properly. (see the [HPC Guide](https://hpcguide.rockefeller.edu/guides/conda.html))

## Sample Data

The sample data used by the jupyter notebook are stored in the `sample-data` file. The file `ls_orchid.fasta` is fairly small and is stored in this repository. To obtain the larger data files you will need for this workshop, run the `get_large_data.py` python file. This uses `wget` to download a large data file, and then generates medium-sized files (compressed and uncompressed) of 500,000 sequences which are used in the notebook to demonstrate how to work with large datasets without excessive time being spent.

You will need to download/create these large and medium sized data files in order to complete the first workshop.

## Creating an environment for this workshop using conda

Start from base in the miniconda command prompt interface (replace the Python version with whichever version you like - I used 3.11). Here, we will create a new environment called biopython, activate is, and install the packages necessary for this workshop.

```
conda create -n biopython python=3.11
conda activate biopython
pip install biopython
pip install ipykernel
pip install wget
```
