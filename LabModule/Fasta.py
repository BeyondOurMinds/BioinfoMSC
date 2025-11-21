class FastaMyPasta:
    def __init__(self, file):
        self._file = file
    
    @property
    def file(self):
        return self._file

    def fileRead(self):
        with open (self.file, 'r') as my_file:
            for line in my_file:
                line = line.rstrip()
                if line.startswith('>'):
                    geneID = line.strip('>').rstrip()
                    seq = my_file.readline().rstrip()
                    yield geneID, seq