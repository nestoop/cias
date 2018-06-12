import numpy as np
import distance as distance


# load file data, data change to matrix
def load_data(file_path):
    f = open(file_path)
    data = []
    for line in f.readlines():
        row = []
        lines = line.strip().split(",")
        for x in lines:
            row.append(float(x))
        data.append(row)
    f.close()
    return np.mat(data)


# count k central
def countCentral(data, k):
    pro_n = np.shape(data)[1]
    print(pro_n)
    # init k matrix and every matrix element is 0
    init_k_central = np.mat(np.zeros((k, pro_n)))
    print(init_k_central)
    for j in xrange(pro_n):
        min_j = np.min(data[:, j])
        rang_j = np.max(data[:, j]) - min_j
        init_k_central[:, j] = min_j * np.mat(np.ones((k, 1))) + np.random.rand(k, 1) * rang_j
    return init_k_central


def kmeans(data, k, countCentral):
    """
    :param data:  train data
    :param k:  k
    :param countCentral: init k cluster
    :return:
    """
    # m line n row matrix
    m, n = np.shape(data)
    subCenter = np.mat(np.zeros((m, 2)))
    change = True

    while change:
        change = False
        for i in xrange(m):
            minDist = np.inf
            minIndex = 0
            for j in xrange(k):
                dist = distance(data(i, ), countCentral(j, ))
                if dist < minDist:
                    minDist = dist
                    minIndex = j
            if subCenter[i,] < minIndex:
                change = True
                subCenter[i,] = np.mat([minIndex, minDist])

        for j in xrange(k):
            sum_all = np.mat(np.zeros(1, n))
            r = 0
            for i in xrange(m):
                if subCenter[i, 0] == j:
                    sum_all += data[i,]
                    r += 1
            for z in xrange(n):
                try:
                    countCentral[j, z] = sum_all[0, z] / r
                except:
                    print("r is zero")

    return countCentral, subCenter
