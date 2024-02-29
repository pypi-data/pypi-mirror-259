# CYP2D6 Parser

The CYP2D6 parser utilizies the recommendations by [PharmVar](https://pubmed.ncbi.nlm.nih.gov/37669183/) to organize *CYP2D6* haplotypes and genotypes. The parsing and sorting of these haplotypes appears simple but many edge cases exist. This tool helps to facillitate the genotype reporting process by providing a standardized approach for reporting haplotypes.

Current tool outputs supported:
1. Aldy
1. Cyrius
1. PyPGx
1. Stargazer
1. StellarPGx


## Installation

Installation can be acheived using pip or any other package manager of your choosing
```sh
pip install cyp2d6_parser 
```

## Parsing genotypes

### API
```python
import cyp2d6_parser

# Provide a genotype. If a caller is known, you can provide it to aid in some parsing
# otherwise just a genotype is fine too, but a warning will be reported
results = cyp2d6_parser.parse_genotype(genotype="*1/*10+*36")

# Provide a file. If supplying a file or directory, must identify the type of caller used
results = cyp2d6_parser.parse_genotype(file='aldy_results.tsv', caller='aldy')

# Can also provide a directory of files using glob patterns
results = cyp2d6_parser.parse_genotype(dir_='aldy_results/*.tsv', caller='aldy', output_file='results.tsv')


# parse_genotype above will report activity score and phenotype
result = cyp2d6_parser.get_activity_score(genotype='*1/*10+*36')

result = cyp2d6_parser.get_phenotype(genotype='*1/*10+*36')
result = cyp2d6_parser.get_phenotype(activity_score=2)
```

### CLI
```sh
python3 -m cyp2d6_parser genotype --genotype_call "*1/*10+*36"

python3 -m cyp2d6_parser --caller aldy genotype --file aldy_results.tsv

python3 -m cyp2d6_parser --caller aldy genotype --dir aldy_results/*.tsv -o results.tsv

python3 -m cyp2d6_parser activity --genotype_call "*1/*10+*36"

python3 -m cyp2d6_parser phenotype --genotype_call "*1/*10+*36"
python3 -m cyp2d6_parser phenotype --activity_score 2
```

## Interpreting output from parse_genotype

1. sample_id - File name or left blank
1. genotype_raw - Genotype(s) used as input, semicolon delimited
1. genotype - Parsed and organized genotype according to PharmVar reccomendations. Retired alleles are converted to the new allele name (Ex: *57 -> *36). If you would like to report retired alleles, an option is available. Suballeles names are removed (Ex: *4.001 -> *4). If a single genotype cannot be resolved, Indeterminate/Indeterminate is reported.
1. activity_score - Total activity score for the reported genotype
1. phenotype - Phenotype based on activity score
1. copy_number - Total number of copies in genotype only if the genotype is not Indeterminate. The only allele which does not count towards total copy number is *5 (gene deletion).
1. possible_genotype - If the input genotypes cannot be resolved to a single genotype, all possible genotypes are reported in this field as semicolon delimited.
1. possible_activity_score - If all possible genotypes resolve to a single activity score, then an activity score is reported
1. possible_phenotype - If all possible activity scores resolve to a single phenotype, then the phenotype is reported. The activity score field can be blank with a possible phenotype. Ex:
    - possible_genotypes: \*1/\*1;\*1/\*10
    - possible_activity_score: not reported because possible values are 2 and 1.25
    - possible_phenotype: CYP2D6 Normal Metabolizer

## Bugs and desired features
Please report any bugs and/or desired features to either the github issues page or to andrew.haddad@pitt.edu