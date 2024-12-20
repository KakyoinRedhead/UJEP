from string import ascii_lowercase
from collections import Counter

# write open("string," 'r') as soubor:
#   obsah = soubor.read
#   return obsah

#obsah 
string = "Ahojjjjj jak je hahahaha se zabiju lool"

pocet_pismen = Counter(string)

for pismeno in ascii_lowercase:
    print(f'{pismeno} = {pocet_pismen.get(pismeno, 0)}')

