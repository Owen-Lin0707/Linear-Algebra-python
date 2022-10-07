import scipy.sparse
import numpy as np

def p1_has_cycle(sets):
  mx = scipy.sparse.csr_matrix(sets) # convert to csr_matrix
  row_num = mx.shape[0] # to get the number of rows of the matrix 
  while row_num > 1:
    one_idx = np.where(mx.getrow(0).toarray() == 1)[1] # to find the index of 1 in the first row
    add_rows = np.where(mx.getcol(one_idx).toarray() == -1)[0] # find rows which have -1 at the same index as above
    for row in add_rows:
      new_row = mx.getrow(0) + mx.getrow(row) # add the first row to the rows found above
      if new_row.min() == 0: # if the minimum in new row is zero, which means there's only zero in the new row, then return true
        return True
      mx = scipy.sparse.vstack((mx, new_row)) # otherwise, put the new row to the buttom of the matrix, thus, the number of rows +1
      row_num += 1
    mx = mx[1:] # pop out the first row of the matrix, then the number of rows -1
    row_num -= 1
  return False
  # if the matrix left only 1 row, then the result is false
