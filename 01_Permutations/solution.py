import  itertools

def print_permutations(s):
    # Generate all permutations
    perms = itertools.permutations(s)
    #print(list(perms))

    for perm in perms:
        print(''.join(perm))


s = "ABC"
print_permutations(s)