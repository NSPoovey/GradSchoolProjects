def readDNA(filename):
    DNA = ''
    subString = 'TTCATTCGTT'
    temp = ''
    j = 0
    with open(filename, 'r') as f:
        for line in f:
            if line[0] == '>':
                tmp = line.rstrip()
            if not line[0] == '>':
                DNA += line.rstrip()
                start = len(subString) - 1
                j = start
                i = len(subString) - 1
            while j < len(DNA) -9:
                while subString[i] == DNA[j] and i != 0:
                    i -= 1
                    j -= 1
                if subString[i] == DNA[j] and i == 0:
                    print('Match found in ' + tmp)
                if subString[i] != DNA[j] and DNA[j] == 'T':
                    i = len(subString)-1
                    start += 1
                    j = start
                if subString[i] != DNA[j] and DNA[j] == 'A':
                    i = len(subString)-1
                    start += 6
                    j = start
                if subString[i] != DNA[j] and DNA[j] == 'G':
                    i = len(subString)-1
                    start += 2
                    j = start
                if subString[i] != DNA[j] and DNA[j] == 'C':
                    i = len(subString) -1
                    start += 3
                    j = start


    return DNA
DNA = readDNA('97_otus.fasta')

