from math import log, sqrt
from collections import Counter

def purity(groundtruthAssignment, algorithmAssignment):

    tbl = Counter(list(zip(algorithmAssignment,groundtruthAssignment)))
    tbl = {tuple(s): count for s, count in tbl.most_common()}

    nbAlgCs = len(set([t[0] for t in tbl.keys()]))

    # Compute the purity
    p = 0.0
    for i in range(nbAlgCs):
        l = [tbl[(i, key[1])] for key in tbl.keys() if key[0] == i]
        p += max(l)

    purity = p/len(algorithmAssignment)
    return purity 


def NMI(groundtruthAssignment, algorithmAssignment):

    tbl = Counter(list(zip(algorithmAssignment,groundtruthAssignment)))
    tbl = {tuple(s): count for s, count in tbl.most_common()}

    nbAlgCs = len(set([t[0] for t in tbl.keys()]))
    nbGroundCs = len(set([t[1] for t in tbl.keys()]))

    probCi = [0] * nbAlgCs
    for i in range(nbAlgCs):
        l = [tbl[(i, key[1])]for key in tbl.keys() if key[0] == i]
        probCi[i] = sum(l)/float(len(groundtruthAssignment))
    Hc = -sum([p * log(p) for p in probCi])

    probTj = [0] * nbGroundCs
    for j in range(nbGroundCs):
        l = [tbl[(key[0], j)]for key in tbl.keys() if key[1] == j]
        probTj[j] = sum(l)/float(len(groundtruthAssignment))
    Ht = -sum([p * log(p) for p in probTj])

    # Compute the NMI
    iCT = 0.0
    probIJ = {s: count/float(len(groundtruthAssignment)) for s, count in tbl.iteritems()}
    for i in range(nbAlgCs):
        for j in range(nbGroundCs):
            pij = probIJ[(i, j)]
            iCT += (pij * log(pij/(probCi[i] * probTj[j])))

    NMI = iCT/sqrt(Hc * Ht)
    return NMI
