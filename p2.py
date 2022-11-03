import numpy as np

def get_key(cipher, plain):
  cipher_list = []
  for word in cipher:
    if word >= 'A' and word <= 'Z':
      cipher_list.append(ord(word) - 65)
    elif word == '_':
      cipher_list.append(26)
    elif word == '.':
      cipher_list.append(27)
    elif word == ',':
      cipher_list.append(28)
    elif word == '?':
      cipher_list.append(29)
    elif word == '!':
      cipher_list.append(30)

  length = len(cipher_list)
  if length % 3 == 1:
    cipher_list.append(cipher_list[length - 1])
    cipher_list.append(cipher_list[length - 1])
  if length % 3 == 2:
    cipher_list.append(cipher_list[length - 1])
  
  arr_c = np.array(cipher_list)
  arr_c = np.reshape(arr_c, (-1, 3)).T

  plain_list = []
  for word in plain:
    if word >= 'A' and word <= 'Z':
      plain_list.append(ord(word) - 65)
    elif word == '_':
      plain_list.append(26)
    elif word == '.':
      plain_list.append(27)
    elif word == ',':
      plain_list.append(28)
    elif word == '?':
      plain_list.append(29)
    elif word == '!':
      plain_list.append(30)

  length = len(plain_list)
  if length % 3 == 1:
    plain_list.append(plain_list[length - 1])
    plain_list.append(plain_list[length - 1])
  if length % 3 == 2:
    plain_list.append(plain_list[length - 1])
  
  arr_p = np.array(plain_list)
  arr_p = np.reshape(arr_p, (-1, 3)).T

  arr_a = np.dot(arr_c, mod_inv(arr_p))
  arr_a = np.ravel(arr_a)

  key = ''
  for i in range(9):
    arr_a[i] = arr_a[i] % 31
    key += str(arr_a[i])
    if i != 8:
      key += ' '
      
  return key
