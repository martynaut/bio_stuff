#!/usr/bin/env python
# -*- coding: utf-8 -*-

def rev_comp_change(change_type, NA, seq):
	for i in seq.upper():
		if i not in ['A', 'T', 'C', 'G', 'U']:
			return 'wrong sequence'

	seq = seq.upper()
	dna_rna_dict = {
	'T' : 'U',
	'U' : 'U',
	'C' : 'C',
	'G' : 'G',
	'A' : 'A'
	}
	rna_dna_dict = {
	'T' : 'T',
	'U' : 'T',
	'C' : 'C',
	'G' : 'G',
	'A' : 'A'
	}	
	dna_dict = {
	'A' : 'T',
	'T' : 'A',
	'C' : 'G',
	'G' : 'C',
	'U' : 'A'
	}
	rna_dict = {
	'A' : 'U',
	'T' : 'A',
	'C' : 'G',
	'G' : 'C',
	'U' : 'A'
	}
	if NA == "RNA":
		seq = ''.join(dna_rna_dict[x] for x in seq)
	elif NA == 'DNA':
		seq = ''.join(rna_dna_dict[x] for x in seq)
	if change_type == 'complementary' or change_type == 'reverse complementary':
		print('a')
		if NA == "DNA":
			seq = ''.join(dna_dict[x] for x in seq)
		elif NA == "RNA":
			seq = ''.join(rna_dict[x] for x in seq)

	if change_type == 'reverse complementary' or change_type == 'reverse':
		seq = seq[::-1]
	return seq