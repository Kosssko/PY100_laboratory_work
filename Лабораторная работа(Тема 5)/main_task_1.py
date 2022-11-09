# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
stat = 0
finish = 15
dict_ = [{'bin': bin(number), 'dec': number, 'hex': hex(number), 'oct': oct(number)} for number in range(stat, finish+1)]
pprint(dict_) 