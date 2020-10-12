"""
Run each component of inDephi to understand its inputs/outputs
"""

# zzjfrank, 2020-10-11

from inDelphi import init_model, predict

# the example sequence in inDelphi webserver
left = 'GCAGTCAGTGCAGTAGAGGATGTGTCGCTCTCCCGTACGGCGTGAAAATGACTAGCAAAG'
right = 'TTGGGGCCTTTTTGGAAGACCTAGAGCCTTAGGCCACGGTACACAATGGTGTCCTGCATA'
seq = left + right
cutsite = len(left)

pred_df, stats = predict(seq, cutsite)