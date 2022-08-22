#!/usr/bin/env python3

# Inputs
inputs = [
	'a',
	'bb',
	'ccc',
	'dddd',
	'eeeee',
]


# Function
def bigger_than_three(string):
	return True if len(string) > 3 else False

# Filter
result = filter(bigger_than_three, inputs)
print(result)
print(list(result))