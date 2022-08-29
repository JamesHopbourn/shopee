#!/usr/bin/env python3

import string
from random import choice

sets, character = [],[string.ascii_lowercase, string.ascii_uppercase, string.digits]
[sets.append(i[j]) for i in character for j in range(len(i))]
[character.append(choice(sets)) for i in range(16)]
print(''.join(character[-16:]))