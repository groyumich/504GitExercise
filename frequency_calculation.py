def get_basecounts_dict(a):
    '''
    Creates a dictionary containing each base in the string and their counts
    '''
    base_dict = dict()
    for c in a:
        if c not in base_dict:
            base_dict[c] = 1
        else:
            base_dict[c] += 1
    return base_dict

def get_freq(a):
    '''
    Prints out the proportional frequency of each base in a provided dictionary of
    bases and counts.
    '''
    print('freqs')
    total = float(sum([a[b] for b in a.keys()]))
    for b in a.keys():
        print(b + ':' + str(a[b]/total))

basecounts = 'ATCTGACGCGCGCCGC'
basecounts_dict = get_basecounts_dict(basecounts)
get_freq(basecounts_dict)
