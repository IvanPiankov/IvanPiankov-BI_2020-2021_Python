class DNA:
    type = "DNA"
    def __init__(self, sequence):
        self.sequence = sequence.upper()
        self.length = len(sequence)
        if "U" in self.sequence:
            raise SyntaxError("DNA does not contain U")
    def gc_content(self):
        return f"GC content = {((self.sequence.count('G') + self.sequence.count('C')) / len(self.sequence)) * 100}%"
    def reverse_complement(self):
        complement = {'A': 'T','T': 'A', 'C': 'G', 'G': 'C'}
        return "".join([complement[k] for k in self.sequence[::-1]])
    def __iter__(self):
        self.iter = 0
        return self
    def __next__(self):
        if self.iter < len(self.sequence):
            result = self.sequence[self.iter]
            self.iter += 1
            return result
        else:
            raise StopIteration
    def __eq__(self, other):
        return self.sequence == other.sequence
    def __hash__(self):
        return hash(self.sequence)
    def transcribe(self):
        sequence = self.sequence.replace("T", "U")
        return RNA(sequence)

class RNA:
    type = "RNA"
    def __init__(self, sequence):
        self.sequence = sequence.upper()
        self.length = len(sequence)
        if "T" in self.sequence:
            raise SyntaxError("RNA does not contain T")
    def gc_content(self):
        return f"GC content = {((self.sequence.count('G') + self.sequence.count('C')) / len(self.sequence)) * 100}%"
    def reverse_complement(self):
        complement = {'A': 'U','U': 'A', 'C': 'G', 'G': 'C'}
        return "".join([complement[k] for k in self.sequence[::-1]])
    def __iter__(self):
        self.iter = 0
        return self
    def __next__(self):
        if self.iter < len(self.sequence):
            result = self.sequence[self.iter]
            self.iter += 1
            return result
        else:
            raise StopIteration
    def __eq__(self, other):
        return self.sequence == other.sequence
    def __hash__(self):
        return hash(self.sequence)

