import os
import unittest
from cyp2d6_parser import parser

PATH = os.path.dirname(os.path.abspath(__file__))


class TestFiles(unittest.TestCase):

    def test_aldy(self):
        results = parser.parse_genotype(
            file=os.path.join(PATH, "test_files", "aldy.tsv"), caller="aldy"
        )
        self.assertEqual(results.loc[0, "genotype"], "*1/*4")

    def test_cyrius(self):
        results = parser.parse_genotype(
            file=os.path.join(PATH, "test_files", "cyrius.tsv"), caller="cyrius"
        )
        self.assertEqual(results.loc[0, "genotype"], "*1/*4")

    def test_pypgx(self):
        results = parser.parse_genotype(
            file=os.path.join(PATH, "test_files", "pypgx.zip"), caller="pypgx"
        )
        self.assertEqual(results.loc[0, "genotype"], "*1/*36+*10")

    def test_stellarpgx(self):
        results = parser.parse_genotype(
            file=os.path.join(PATH, "test_files", "stellarpgx.alleles"),
            caller="stellarpgx",
        )
        self.assertEqual(results.loc[0, "genotype"], "*1/*4")
