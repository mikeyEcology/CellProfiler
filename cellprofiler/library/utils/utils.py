import numpy

def create_ijv(dense):
    """Convert a dense label into an ijv format"""
    ijv = []
    # Find all non-background (0) labels within dense and 
    # append to ijv
    for i in range(dense.shape[0]):
        for j in range(dense.shape[1]):
            value = dense[i, j]
            if value != 0:
                ijv.append((j, i, value))
    # Return the resulting ijv array
    return numpy.array(ijv)