
def kmer2str(val, k):
    """ Transform a kmer integer into a its string representation
    :param int val: An integer representation of a kmer
    :param int k: The number of nucleotides involved into the kmer.
    :return str: The kmer string formatted
    """
    letters = ['A', 'C', 'G', 'T']
    str_val = []
    for _ in range(k):
        str_val.append(letters[val & 0b11])
        val >>= 2

    str_val.reverse()
    return "".join(str_val)

def encode_nuc(nuc):
    """ Transform a nucleotide character into its integer representation
    :param str nuc: A character representing a nucleotide
    :return int: The nucleotide integer formatted
    """
    letters = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    return letters[nuc]


def encode_kmer(seq, k):
    """ Transform a kmer string into its integer representation and its reverse complement.
    :param str seq: A string representation of a kmer
    :param int k: The number of nucleotides involved in the kmer.
    :return int : The integer representations of the kmer and its reverse complement.
    """
    kmer = 0
    kmer_r = 0
    
    for i in range(k):
        nuc = seq[i]   
        kmer <<= 2 
        kmer |= encode_nuc(nuc)  
    
    return kmer


def reverse_kmer(kmer, k):
    """Reverse the k-mer by reversing its bits, as if it represents the reverse complement
    of the k-mer.
    :param int kmer: The k-mer encoded as an integer
    :param int k: The length of the k-mer
    :return int: The reverse complement k-mer as an integer
    """
    reverse = 0

    for _ in range(k):
        reverse <<= 2
        reverse |= (~kmer & 3)   # ~kmer is the reverse of kmer, and 3 is the mask for 2 bits (where 01 is 10 and 00 is 11)
        kmer >>= 2
    
    return reverse

def stream_kmers(seq, k):

    
    mask = (1<<(2*(k-1)))-1 
    kmer_d = encode_kmer(seq, k)
    kmer_r = reverse_kmer(kmer_d, k)
    kmer = min(kmer_d, kmer_r)
    for i in range (len(seq)-(k)):
        yield kmer
        kmer_d&=mask
        kmer_d <<=2
        kmer_d |= encode_nuc(seq[i+k])
        kmer_r = reverse_kmer(kmer_d, k)
        kmer = min(kmer_d, kmer_r)
       
    yield kmer


def create_index(seq, k):
    index = {}
    for kmer in stream_kmers(seq, k):
        if kmer in index:
            index[kmer] += 1
        else:
            index[kmer] = 1
    return index
    

