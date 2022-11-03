import numpy as np

def decode(cipher, key):
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

  key_slist = key.split(' ')
  key_list = []
  for s in key_slist:
    key_list.append(int(s))

  arr_a = np.array(key_list)
  arr_a = np.reshape(arr_a, (3, 3))
  
  arr_p = np.dot(mod_inv(arr_a), arr_c).T
  arr_p = np.ravel(arr_p)

  plain = ''
  for num in arr_p:
    num = num % 31
    if num >= 0 and num <= 25:
      plain += chr(num + 65)
    elif num == 26:
      plain += '_'
    elif num == 27:
      plain += '.'
    elif num == 28:
      plain += ','
    elif num == 29:
      plain += '?'
    elif num == 30:
      plain += '!'
      
  return plain
