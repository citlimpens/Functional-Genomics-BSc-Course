#!/usr/bin/python

#Cilalli Limpens

#ejercicio 5 tarea

Transcrito = "ATAATTGGACAGGTCTGGGATCCGGTCCCCTGCTCAGACCCCGGAGGCTAAGGAGTTGTTTCGGAAGGAGCTGACAGCTTTTCCTTCCGCAGACTGGCCAATCACAACTGGGAAGATGAAGGCTCTGTGGGCCCTGCTGTTGGTCCCATTGCTGACAGGATGCCTGGCCGAGGGAGAGCTGGAGGTGACAGATCAGCTCCCAGGGCAAAGCGACCAACCCTGGGAGCAGGCCCTGAACCGCTTCTGGGATTACCTGCGCTGGGTGCAGACGCTTTCTGACCAGGTCCAGGAAGAGCTGCAGAGCTCCCAAGTCACACAGGAACTGACGGTACTGATGGAGGACACTATGACGGAAGTAAAGGCATACAAAAAGGAGCTGGAGGAACAGCTGGGCCCAGTGGCGGAGGAGACACGGGCCAGGCTGGCTAAAGAGGTGCAGGCGGCACAGGCCCGTCTGGGAGCTGACATGGAGGATCTACGCAACCGACTCGGGCAGTACCGCAACGAGGTAAACACCATGCTGGGCCAGAGCACAGAGGAGCTGCGGTCGCGCCTCTCCACACACCTGCGCAAGATGCGCAAGCGCCTGATGCGGGATGCGGATGATCTGCAGAAGCGCCTGGCGGTGTACAAGGCCGGGGCACAGGAGGGCGCCGAGCGCGGTGTGAGTGCTATCCGTGAGCGCCTGGGGCCACTGGTGGAGCAGGGTCGTCAGCGCACAGCCAACCTAGGCGCTGGCGCCGCCCAGCCCCTGCGCGATCGCGCCCAGGCTTTGAGTGACCGCATCCGAGGGCGGCTGGAGGAAGTGGGCAACCAGGCCCGAGACCGCCTAGAGGAGGTGCGTGAGCAGATGGAGGAGGTGCGCTCCAAGATGGAGGAGCAGACCCAGCAGATACGCCTGCAGGCCGAGATCTTCCAGGCCCGCATCAAGGGCTGGTTCGAGCCGCTAGTGGAAGACATGCAGCGCCAGTGGGCAAACCTAATGGAGAAGATACAGGCCTCTGTGGCTACCAACTCCATTGCCTCCACCACAGTGCCCCTGGAGAATCAATGATCATCCCTCACCTACGCCCTGCCGCAACATCCATGACCAGCCAGGTGGCCCTGTCCCAAGCACCACTCTGGCCCTCTGGTGGCCCTTGCTTAATAAAGATTCTCCAAGCAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

P1 = ""
P2 = ""
P3 = ""


M = ["ATG"]
F = ["TTT", "TTC"]
L = ["TTA", "TTG", "CTT", "CTC", "CTA", "CTG"]
I = ["ATT", "ATC", "ATA"]
V = ["GTT", "GTC", "GTA", "GTG"]
S = ["TCT", "TCC", "TCA", "TCG", "AGT", "AGG"]
P = ["CCT", "CCC", "CCA", "CCG"]
T = ["ACT", "ACC", "ACA", "ACG"]
A = ["GCT", "GCC", "GCA", "GCG"]
Y = ["TAT", "TAC"]
H = ["CAT", "CAC"]
Q = ["CAA", "CAG"]
N = ["AAT", "AAC"]
K = ["AAA", "AAG"]
D = ["GAT", "GAC"]
E = ["GAA", "GAG"]
C = ["TGT", "TGC"]
W = ["TGG"]
R = ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"]
G = ["GGT", "GGC", "GGA", "GGG"]

END = ["TAA", "TAG", "TGA"]

ciclos = 0

while ciclos < len(Transcrito):
	condicional = Transcrito[ciclos] + Transcrito[ciclos + 1] + Transcrito[ciclos + 2]
	if condicional in M:
		P1 = P1 + "M"
	elif condicional in F:
		P1 = P1 + "F"
	elif condicional in L:
		P1 = P1 + "L"
	elif condicional in I:
		P1 = P1 + "I"
	elif condicional in V:
		P1 = P1 + "V"
	elif condicional in S:
		P1 = P1 + "S"
	elif condicional in P:
		P1 = P1 + "P"
	elif condicional in T:
		P1 = P1 + "T"
	elif condicional in A:
		P1 = P1 + "A"
	elif condicional in Y:
		P1 = P1 + "Y"
	elif condicional in H:
		P1 = P1 + "H"
	elif condicional in Q:
		P1 = P1 + "Q"
	elif condicional in N:
		P1 = P1 + "N"
	elif condicional in K:
		P1 = P1 + "K"
	elif condicional in D:
		P1 = P1 + "D"
	elif condicional in E:
		P1 = P1 + "E"
	elif condicional in C:
		P1 = P1 + "C"
	elif condicional in W:
		P1 = P1 + "W"
	elif condicional in R:
		P1 = P1 + "R"
	elif condicional in G:
		P1 = P1 + "G"
	elif condicional in END:
		P1 = P1 + "*"
	else:
		P1 = P1 + "_"
	ciclos = ciclos + 3

print "\n", P1

ciclos = 1
while ciclos < len(Transcrito):
	condicional = Transcrito[ciclos] + Transcrito[ciclos + 1] + Transcrito[ciclos + 2]
	if condicional in M:
		P2 = P2 + "M"
	elif condicional in F:
		P2 = P2 + "F"
	elif condicional in L:
		P2 = P2 + "L"
	elif condicional in I:
		P2 = P2 + "I"
	elif condicional in V:
		P2 = P2 + "V"
	elif condicional in S:
		P2 = P2 + "S"
	elif condicional in P:
		P2 = P2 + "P"
	elif condicional in T:
		P2 = P2 + "T"
	elif condicional in A:
		P2 = P2 + "A"
	elif condicional in Y:
		P2 = P2 + "Y"
	elif condicional in H:
		P2 = P2 + "H"
	elif condicional in Q:
		P2 = P2 + "Q"
	elif condicional in N:
		P2 = P2 + "N"
	elif condicional in K:
		P2 = P2 + "K"
	elif condicional in D:
		P2 = P2 + "D"
	elif condicional in E:
		P2 = P2 + "E"
	elif condicional in C:
		P2 = P2 + "C"
	elif condicional in W:
		P2 = P2 + "W"
	elif condicional in R:
		P2 = P2 + "R"
	elif condicional in G:
		P2 = P2 + "G"
	elif condicional in END:
		P2 = P2 + "*"
	else:
		P2 = P2 + "_"
	ciclos = ciclos + 3

print "\n", P2

ciclos = 2
while ciclos < len(Transcrito):
	condicional = Transcrito[ciclos] + Transcrito[ciclos + 1] + Transcrito[ciclos + 2]
	if condicional in M:
		P3 = P3 + "M"
	elif condicional in F:
		P3 = P3 + "F"
	elif condicional in L:
		P3 = P3 + "L"
	elif condicional in I:
		P3 = P3 + "I"
	elif condicional in V:
		P3 = P3 + "V"
	elif condicional in S:
		P3 = P3 + "S"
	elif condicional in P:
		P3 = P3 + "P"
	elif condicional in T:
		P3 = P3 + "T"
	elif condicional in A:
		P3 = P3 + "A"
	elif condicional in Y:
		P3 = P3 + "Y"
	elif condicional in H:
		P3 = P3 + "H"
	elif condicional in Q:
		P3 = P3 + "Q"
	elif condicional in N:
		P3 = P3 + "N"
	elif condicional in K:
		P3 = P3 + "K"
	elif condicional in D:
		P3 = P3 + "D"
	elif condicional in E:
		P3 = P3 + "E"
	elif condicional in C:
		P3 = P3 + "C"
	elif condicional in W:
		P3 = P3 + "W"
	elif condicional in R:
		P3 = P3 + "R"
	elif condicional in G:
		P3 = P3 + "G"
	elif condicional in END:
		P3 = P3 + "*"
	else:
		P3 = P3 + "_"
	ciclos = ciclos + 3

print "\n", P3

def revcom (seq):
    rev = seq[::-1]
    from string import maketrans
    t = maketrans('ACGT', 'TGCA')
    rc = rev.translate(t)
    return rc
    
s = 'ATAATTGGACAGGTCTGGGATCCGGTCCCCTGCTCAGACCCCGGAGGCTAAGGAGTTGTTTCGGAAGGAGCTGACAGCTTTTCCTTCCGCAGACTGGCCAATCACAACTGGGAAGATGAAGGCTCTGTGGGCCCTGCTGTTGGTCCCATTGCTGACAGGATGCCTGGCCGAGGGAGAGCTGGAGGTGACAGATCAGCTCCCAGGGCAAAGCGACCAACCCTGGGAGCAGGCCCTGAACCGCTTCTGGGATTACCTGCGCTGGGTGCAGACGCTTTCTGACCAGGTCCAGGAAGAGCTGCAGAGCTCCCAAGTCACACAGGAACTGACGGTACTGATGGAGGACACTATGACGGAAGTAAAGGCATACAAAAAGGAGCTGGAGGAACAGCTGGGCCCAGTGGCGGAGGAGACACGGGCCAGGCTGGCTAAAGAGGTGCAGGCGGCACAGGCCCGTCTGGGAGCTGACATGGAGGATCTACGCAACCGACTCGGGCAGTACCGCAACGAGGTAAACACCATGCTGGGCCAGAGCACAGAGGAGCTGCGGTCGCGCCTCTCCACACACCTGCGCAAGATGCGCAAGCGCCTGATGCGGGATGCGGATGATCTGCAGAAGCGCCTGGCGGTGTACAAGGCCGGGGCACAGGAGGGCGCCGAGCGCGGTGTGAGTGCTATCCGTGAGCGCCTGGGGCCACTGGTGGAGCAGGGTCGTCAGCGCACAGCCAACCTAGGCGCTGGCGCCGCCCAGCCCCTGCGCGATCGCGCCCAGGCTTTGAGTGACCGCATCCGAGGGCGGCTGGAGGAAGTGGGCAACCAGGCCCGAGACCGCCTAGAGGAGGTGCGTGAGCAGATGGAGGAGGTGCGCTCCAAGATGGAGGAGCAGACCCAGCAGATACGCCTGCAGGCCGAGATCTTCCAGGCCCGCATCAAGGGCTGGTTCGAGCCGCTAGTGGAAGACATGCAGCGCCAGTGGGCAAACCTAATGGAGAAGATACAGGCCTCTGTGGCTACCAACTCCATTGCCTCCACCACAGTGCCCCTGGAGAATCAATGATCATCCCTCACCTACGCCCTGCCGCAACATCCATGACCAGCCAGGTGGCCCTGTCCCAAGCACCACTCTGGCCCTCTGGTGGCCCTTGCTTAATAAAGATTCTCCAAGCAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
r = revcom(s)

print "reverso complementario" r

P1 = ""
P2 = ""
P3 = ""

ciclos = 0

while ciclos < len(r):
	condicional = r[ciclos] + r[ciclos + 1] + r[ciclos + 2]
	if condicional in M:
		P1 = P1 + "M"
	elif condicional in F:
		P1 = P1 + "F"
	elif condicional in L:
		P1 = P1 + "L"
	elif condicional in I:
		P1 = P1 + "I"
	elif condicional in V:
		P1 = P1 + "V"
	elif condicional in S:
		P1 = P1 + "S"
	elif condicional in P:
		P1 = P1 + "P"
	elif condicional in T:
		P1 = P1 + "T"
	elif condicional in A:
		P1 = P1 + "A"
	elif condicional in Y:
		P1 = P1 + "Y"
	elif condicional in H:
		P1 = P1 + "H"
	elif condicional in Q:
		P1 = P1 + "Q"
	elif condicional in N:
		P1 = P1 + "N"
	elif condicional in K:
		P1 = P1 + "K"
	elif condicional in D:
		P1 = P1 + "D"
	elif condicional in E:
		P1 = P1 + "E"
	elif condicional in C:
		P1 = P1 + "C"
	elif condicional in W:
		P1 = P1 + "W"
	elif condicional in R:
		P1 = P1 + "R"
	elif condicional in G:
		P1 = P1 + "G"
	elif condicional in END:
		P1 = P1 + "*"
	else:
		P1 = P1 + "_"
	ciclos = ciclos + 3

print "\n", P1

ciclos = 1
while ciclos < len(r):
	condicional = r[ciclos] + r[ciclos + 1] + r[ciclos + 2]
	if condicional in M:
		P2 = P2 + "M"
	elif condicional in F:
		P2 = P2 + "F"
	elif condicional in L:
		P2 = P2 + "L"
	elif condicional in I:
		P2 = P2 + "I"
	elif condicional in V:
		P2 = P2 + "V"
	elif condicional in S:
		P2 = P2 + "S"
	elif condicional in P:
		P2 = P2 + "P"
	elif condicional in T:
		P2 = P2 + "T"
	elif condicional in A:
		P2 = P2 + "A"
	elif condicional in Y:
		P2 = P2 + "Y"
	elif condicional in H:
		P2 = P2 + "H"
	elif condicional in Q:
		P2 = P2 + "Q"
	elif condicional in N:
		P2 = P2 + "N"
	elif condicional in K:
		P2 = P2 + "K"
	elif condicional in D:
		P2 = P2 + "D"
	elif condicional in E:
		P2 = P2 + "E"
	elif condicional in C:
		P2 = P2 + "C"
	elif condicional in W:
		P2 = P2 + "W"
	elif condicional in R:
		P2 = P2 + "R"
	elif condicional in G:
		P2 = P2 + "G"
	elif condicional in END:
		P2 = P2 + "*"
	else:
		P2 = P2 + "_"
	ciclos = ciclos + 3

print "\n", P2

ciclos = 2
while ciclos < len(r):
	condicional = r[ciclos] + r[ciclos + 1] + r[ciclos + 2]
	if condicional in M:
		P3 = P3 + "M"
	elif condicional in F:
		P3 = P3 + "F"
	elif condicional in L:
		P3 = P3 + "L"
	elif condicional in I:
		P3 = P3 + "I"
	elif condicional in V:
		P3 = P3 + "V"
	elif condicional in S:
		P3 = P3 + "S"
	elif condicional in P:
		P3 = P3 + "P"
	elif condicional in T:
		P3 = P3 + "T"
	elif condicional in A:
		P3 = P3 + "A"
	elif condicional in Y:
		P3 = P3 + "Y"
	elif condicional in H:
		P3 = P3 + "H"
	elif condicional in Q:
		P3 = P3 + "Q"
	elif condicional in N:
		P3 = P3 + "N"
	elif condicional in K:
		P3 = P3 + "K"
	elif condicional in D:
		P3 = P3 + "D"
	elif condicional in E:
		P3 = P3 + "E"
	elif condicional in C:
		P3 = P3 + "C"
	elif condicional in W:
		P3 = P3 + "W"
	elif condicional in R:
		P3 = P3 + "R"
	elif condicional in G:
		P3 = P3 + "G"
	elif condicional in END:
		P3 = P3 + "*"
	else:
		P3 = P3 + "_"
	ciclos = ciclos + 3

print "\n", P3r
