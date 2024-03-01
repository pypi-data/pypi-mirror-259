# PanDots

Pangenome Dotplots. Visualize pangenome chromosome structures by generating dotplots from sequence aligmnets in PAF format.
Sequences should be aligned using the same reference genome.

## Installation
### In a conda environment
Fist create an environment that includes all dependencies:
```
conda create -c conda-forge -c bioconda -n pandots \
  python pandas numpy seaborn plotnine=0.12.4 
```
Then install with `pip`:
```
conda activate pandots
pip install pandots
```

### With just pip
Install  with `pip`:
```
pip install pandots
```

## Usage
### Generate input files
Create PAF pairwise alignments to an anchor genome for all genomes using minimap2 or your prefered method.
Extract your chromosome of interest from all PAF files and concatenate into a single file.

### Visualize with PanDots
Once you have your chromosome PAF file, you can generate the plot.
```
python pandots.py -p <chromosome.paf> -r <reference_chromosome> -o <output_suffix>
```
After completion the plot will be saved as `<output_prefix>.pandots.svg`.

### Aditional arguments
- `-p`,`--paf`: path to paf file for a single chromosome.
- `-r`,`--refchrom`: reference chromosome name
- `-o`,`--outprefix`: output prefix name
- `--key`: flag to include genome key
- `--pad`: integer value to adjust spacing between genomes. Default: 10000000
- `--flip`: flag to make paf column 6 the reference. Column 1 is the reference by default.
- `--invert`: flag to invert reference coordinates in relation to the pangenome.
- `--reorder`: flag to adjust the order of genomes by length and number of invsersions.
- `--recolor`: flag to plot using alternating colors.
- `--orient`: path to two column orientation table (col1=chromosome name, col2=True/False). Will invert coordinates in relation to reference genome. 


## License

PanDots is licensed under a [Salk Institute BSD license](LICENSE)
