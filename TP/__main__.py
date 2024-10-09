from TP.loading import load_directory, load_fasta
from TP.kmers import stream_kmers, kmer2str, create_index




def jaccard(fileA, fileB, k):

    J = []
    seq1 = "".join(fileA)
    seq2 = "".join(fileB)
    
            
    index = create_index(seq1,k)
    intersection = 0
    union = sum(index.values())

    for kmer in stream_kmers(seq2,k):

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
    files = load_directory("data")
    k = 21
    
    print("Computing Jaccard similarity for all pairs of samples")
    filenames = list(files.keys())
    
    #print(filenames)
    for i in range(len(files)):
        for j in range(i+1, len(files)):
            J = jaccard(files[filenames[i]], files[filenames[j]], k)
            
            print(filenames[i], filenames[j], J)
