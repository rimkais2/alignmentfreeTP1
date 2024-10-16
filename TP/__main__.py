from TP.loading import load_directory, load_fasta
from TP.kmers import stream_kmers, kmer2str, create_index, filter_smallest




def jaccard(fileA, fileB, k, s):

    J = []
    seq1 = "".join(fileA)
    seq2 = "".join(fileB)
            
    index = create_index(seq1,k,s)
    intersection = 0
    union = sum(index.values())

    for kmer in filter_smallest(seq2,k,s):

        if kmer in index and index[kmer]>0: 
            intersection +=1 
            index [kmer] -= 1

        else:
            union +=1 

    J= intersection/union
    
    return J


if __name__ == "__main__":

    print("Computation of Jaccard similarity between files")

    # Load all the files in a dictionary
    files = load_directory("databis")
    k = 21
    s = 10000
    
    print("Computing Jaccard similarity for all pairs of samples")
    filenames = list(files.keys())
    
    #print(filenames)
    for i in range(len(files)):
        for j in range(i+1, len(files)):
            J = jaccard(files[filenames[i]], files[filenames[j]], k, s)
            
            print(filenames[i], filenames[j], J)
