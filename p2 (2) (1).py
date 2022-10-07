from operator import mul
import scipy.sparse
import numpy as np

def p2_has_cycle(sets):
  mx = scipy.sparse.csr_matrix(sets) # convert to csr_matrix
  nodes_num = mx.shape[0] # to get the number of nodes of the matrix
  mul_mx = mx # set the first matrix to be multipluied itself
  for i in range(nodes_num):
    if (np.sum(mul_mx.diagonal()) == 0): # if the element in the diagonal of the matrix are all zeros, then multiply the results with matrix again 
      mul_mx = mul_mx.dot(mx)
    else:
      return True # if any element in the diagonal of the matrix is not equal to zero, then return true
  return False
  # if multiplying by N times, and still no results, then return false
