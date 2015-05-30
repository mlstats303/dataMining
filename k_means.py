from utils import * 

def computeSSE(data, centers, clusterID):
    sse = 0 
    nData = len(data) 
    for i in range(nData):
        c = clusterID[i]
        sse += squaredDistance(data[i], centers[c]) 
        
    return sse 

def updateClusterID(data, centers):
    nData = len(data)
    nCenter = len(centers)
    
    clusterID = [0] * nData

    infinity = float('inf')

    # assign the closet center to each data point
    for i in range(nData):
        x = data[i]
        minDist = infinity
        for c in range(nCenter):
            dist = squaredDistance(x,centers[c])
            if dist < minDist:
                clusterID[i] = c
                minDist = dist

    return clusterID

# K: number of clusters 
def updateCenters(data, clusterID, K):
    nDim = len(data[0])
    nData = len(data)
    nC = [0] * K

    centers = [[0] * nDim for _ in range(K)]

    # If a cluster doesn't have any data points, in this homework, leave it to ALL 0s
    for i in range(nData):
        x = data[i]
        c = clusterID[i]
        centroid = centers[c]
        nC[c] += 1

        for k in range(nDim):
            centroid[k] += x[k]
        centers[c] = centroid

    for c in range(K):
        if nC[c] > 0:
            centroid = centers[c]
            for k in range(nDim):
                centroid[k] /= float(nC[c])
            centers[c] = centroid

    return centers

def kmeans(data, centers, maxIter = 100, tol = 1e-6):
    nData = len(data) 
    
    if nData == 0:
        return [];

    K = len(centers) 
    
    clusterID = [0] * nData
    
    if K >= nData:
        for i in range(nData):
            clusterID[i] = i
        return clusterID

    lastDistance = 1e100
    
    for iter in range(maxIter):
        clusterID = updateClusterID(data, centers) 
        centers = updateCenters(data, clusterID, K)
        
        curDistance = computeSSE(data, centers, clusterID) 
        if lastDistance - curDistance < tol or (lastDistance - curDistance)/lastDistance < tol:
            print "# of iterations:", iter 
            print "SSE = ", curDistance
            return clusterID
        
        lastDistance = curDistance
        
    print "# of iterations:", iter 
    print "SSE = ", curDistance
    return clusterID

