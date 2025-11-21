if __name__ == '__main__':
    print('This is the Utils file')


class Sequence:
    def __init__(self, id, seq):
        self._id = id
        self._seq = seq.upper()
    def make_fasta(self):
        return f'>{self.id}\n{self.seq}\n'
    @property
    def id(self):
        return self._id
    @property
    def seq(self):
         return self._seq

class Translates(Sequence):
    def protein(self):
        # make a codon table
        bases = "tcag".upper()
        codons = [a + b + c for a in bases for b in bases for c in bases]
        amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
        codon_table = dict(zip(codons, amino_acids))

        # codon_table is a dict containing codons and amino acids
        proteins = ''
        for i in range(0,len(self.seq),3): # range(start,stop,step) step of 3 to get every third index
            codon=(self.seq[i:i+3]) # defines the codon starting at that index (3 letters)
            if len(codon) < 3: # if thre are any remaining one or two bases at end of sequence, they will not be included in codon list
                break
            amino=codon_table[codon] # calls on the dictionary codon_table for the key of codon, which was defined above, which outputs the corresponding amino acid value and stores it to amino
            proteins += amino # appends that amino to the protein list
        return proteins

class DNA(Sequence):
    def calculateGC(self):
        seqLength = len(self.seq)
        c_count = self.seq.count('C')
        g_count = self.seq.count('G')
        gc_content = ((c_count + g_count) / seqLength) * 100
        return gc_content
    def codon_list_get(self):
        codon_list=[] # create an empty list to store all of the codons
        for i in range(0,len(self.seq),3): # range(start,stop,step) step of 3 to get every third index
            codons=(self.seq[i:i+3]) # prints the codon starting at that index (3 letters)
            if len(codons) < 3: # if thre are any remaining one or two bases at end of sequence, they will not be included in codon list
                break
            codon_list.append(codons) # add the codon to the list
        return codon_list
    def at_cont_get(self):
        A_count=self.seq.count('A')
        T_count=self.seq.count('T')
        AT_cont=((A_count+T_count)/len(self.seq))
        return AT_cont