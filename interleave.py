def interleave(*iter_param):
    return [val for obj in zip(*iter_param) for val in obj]


print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
