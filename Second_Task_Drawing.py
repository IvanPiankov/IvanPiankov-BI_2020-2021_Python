from Bio import SeqIO
import seaborn as sns
import matplotlib.pyplot as plt
import sys

# Second Task
seq_dict = [len(rec.seq) for rec in SeqIO.parse(sys.argv[1], "fasta")]
fig, ax = plt.subplots(1, 1, figsize = (10, 10), dpi=100)
sns.histplot(data=seq_dict, palette='Blues').set_title(f"Sequence Length Distribution")
ax.set_xlabel('Sequence Length (bp)')
ax.set_ylabel("Count of sequence")
plt.show()



