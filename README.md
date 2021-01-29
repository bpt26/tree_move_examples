To use for testing UShER on tree move examples. Run `python makeTreeMoveTestExamples.py example1.txt` to yield a set of 2 fasta files corresponding to the example given. Example files should follow this format:

S1	m1,m2  
S2	m1?,m3

etc., with mutations ending in ? conveted to non-N ambiguous characters.

Example pipeline:

`python makeTreeMoveTestExamples.py example1.txt`
`faToVcf example1_1.fa example1_1.vcf`
`faToVcf example1_2.fa example1_2.vcf`
Then use UShER to create a tree from example1_1.vcf and add samples from example1_2.vcf to that tree.