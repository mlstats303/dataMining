from utils import * 
from math import exp 

def kernel(data, sigma):
    nData = len(data)
    Gram = [[0] * nData for _ in range(nData)]

    # Calculate the Gram matrix
    for i in range(nData):
        Gram[i][i] = 1.0
        for j in range(i+1, nData):
            Gram[i][j] = exp(-squaredDistance(data[i], data[j])/(2.0*sigma*sigma))
            Gram[j][i] = Gram[i][j]

    return Gram


