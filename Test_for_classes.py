import unittest
from DNA_RNA_classes import DNA, RNA


class TestingClassDNA(unittest.TestCase):
    def test_dna_type(self):
        dna = DNA('ATCG')
        self.assertTrue(type(dna), DNA)

    def test_dna_nucleotides(self):
        dna = DNA('ATCG')
        self.assertEqual(dna.sequence, 'ATCG')

    def test_not_dna_nucleotides(self):
        self.assertRaises(SyntaxError, DNA, 'ATUG')

    def test_dna_sequence_upper(self):
        dna = DNA('AtCg')
        self.assertEqual(dna.sequence, 'ATCG')

    def test_dna_length(self):
        dna = DNA('ATCG')
        self.assertEqual(dna.length, 4)

    def test_gc_content(self):
        dna = DNA('ATCG')
        self.assertEqual(dna.gc_content(), f"GC content = 50.0%")

    def test_reverse_complement(self):
        dna = DNA('ATGC')
        self.assertEqual(dna.reverse_complement(), 'GCAT')

    def test_transcribe(self):
        dna = DNA('ATGC')
        self.assertEqual(dna.transcribe(), RNA('AUGC'))

    def test_equal(self):
        self.assertEqual(DNA('ATCG'), DNA('ATCG'))

    def test_not_equal(self):
        self.assertNotEqual(DNA('ATGC'), DNA('ATTTTTTGC'))

    def test_hash(self):
        dna = DNA('ATCG')
        other_dna = DNA('ATCG')
        self.assertEqual(hash(dna), hash(other_dna))

    def test_iterable(self):
        dna = DNA('ATCG')
        self.assertListEqual([x for x in dna.sequence], ['A', 'T', 'C', 'G'])


class TestingClassRNA(unittest.TestCase):

    def test_rna_type(self):
        rna = RNA('AUGC')
        self.assertTrue(type(rna), RNA)

    def test_rna_nucleotides(self):
        rna = RNA('AUGC')
        self.assertEqual(rna.sequence, 'AUGC')

    def test_not_rna_nucleotides(self):
        self.assertRaises(SyntaxError, RNA, 'ATCG')

    def test_rna_sequence(self):
        rna = RNA('AugC')
        self.assertEqual(rna.sequence, 'AUGC')

    def test_rna_sequence_length(self):
        rna = RNA('AUGC')
        self.assertEqual(rna.length, 4)

    def test_gc_content(self):
        rna = RNA('AUGC')
        self.assertEqual(rna.gc_content(), f"GC content = 50.0%")

    def test_reverse_complement(self):
        rna = RNA('AUGC')
        self.assertEqual(rna.reverse_complement(), 'GCAU')

    def test_equal(self):
        self.assertEqual(RNA('AUGC'), RNA('AUGC'))

    def test_not_equal(self):
        self.assertNotEqual(RNA('AUGC'), RNA('AUUUUUGC'))

    def test_hash(self):
        rna = RNA('AUGC')
        other_rna = RNA('AUGC')
        self.assertEqual(hash(rna), hash(other_rna))

    def test_iterable(self):
        rna = RNA('AUGC')
        self.assertListEqual([x for x in rna.sequence], ['A', 'U', 'G', 'C'])


if __name__ == '__main__':
    unittest.main()