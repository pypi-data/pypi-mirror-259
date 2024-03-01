import unittest
from cyp2d6_parser import genotype
from cyp2d6_parser.common import BAD_GENOTYPES


class TestGenotype(unittest.TestCase):

    def test_tandem_order(self):
        # *36+*10
        result = genotype.CYP2D6Genotype(genotypes_raw=["*36+*10/*1"])
        self.assertEqual(result.genotype, "*1/*36+*10")

        # *68+*4
        result = genotype.CYP2D6Genotype(genotypes_raw=["*2/*4+*68"])
        self.assertEqual(result.genotype, "*2/*68+*4")

        # *13+*68+*4
        result = genotype.CYP2D6Genotype(genotypes_raw=["*2/*13+*68+*4"])
        self.assertEqual(result.genotype, "*2/*13+*68+*4")

    def test_genotype_order(self):
        # Genotype order is all about downstream allele
        result = genotype.CYP2D6Genotype(genotypes_raw=["*68+*4/*9x2"])
        self.assertEqual(result.genotype, "*68+*4/*9x2")
        result = genotype.CYP2D6Genotype(genotypes_raw=["*68+*4/*4+*1"])
        self.assertEqual(result.genotype, "*1+*4/*68+*4")

        # Allele with no tandem or cn is always first
        result = genotype.CYP2D6Genotype(genotypes_raw=["*2x3/*2"])
        self.assertEqual(result.genotype, "*2/*2x3")

        # Genotype order is number based not string based
        result = genotype.CYP2D6Genotype(genotypes_raw=["*11/*2"])
        self.assertEqual(result.genotype, "*2/*11")

    def test_retired_alleles(self):
        result = genotype.CYP2D6Data(
            genotypes_raw=["*57/*1"], mask_retired_alleles=False
        )
        self.assertEqual(result.genotype_data.genotype, "*1/*57")
        self.assertEqual(result.phenotype_data.activity_score, 1)

    def test_bad_genotypes(self):
        for bad_genotype in BAD_GENOTYPES:
            result = genotype.CYP2D6Genotype(genotypes_raw=[bad_genotype])
            self.assertEqual(result.genotype, "Indeterminate/Indeterminate")
