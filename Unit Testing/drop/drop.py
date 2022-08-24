# drop.py
import sys
 
drop_file = sys.argv[1]
print(f'You dropped {drop_file}')
with open(drop_file) as f:
    print(f.read())
input('Press <Enter> to exit')