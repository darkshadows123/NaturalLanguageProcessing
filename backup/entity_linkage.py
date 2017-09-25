import numpy as np
import csv

def levenshtein(source, target):
    if len(source) < len(target):
        return levenshtein(target, source)

    # So now we have len(source) >= len(target).
    if len(target) == 0:
        return len(source)

    # We call tuple() to force strings to be used as sequences
    # ('c', 'a', 't', 's') - numpy uses them as values by default.
    source = np.array(tuple(source))
    target = np.array(tuple(target))

    # We use a dynamic programming algorithm, but with the
    # added optimization that we only need the last two rows
    # of the matrix.
    previous_row = np.arange(target.size + 1)
    for s in source:
        # Insertion (target grows longer than source):
        current_row = previous_row + 1

        # Substitution or matching:
        # Target and source items are aligned, and either
        # are different (cost of 1), or are the same (cost of 0).
        current_row[1:] = np.minimum(
                current_row[1:],
                np.add(previous_row[:-1], target != s))

        # Deletion (target grows shorter than source):
        current_row[1:] = np.minimum(
                current_row[1:],
                current_row[0:-1] + 1)

        previous_row = current_row

    return previous_row[-1]


print ("Results for levenshtein") 
print (levenshtein('Battelle'.lower(), 'Battelle\u2019s'))
# with open('company-extractions.txt', 'rU') as f:
#     reader = csv.reader(f, delimiter='\t', dialect=csv.excel_tab)
#     for row in reader:  
#         if levenshtein('Battelle'.lower(), row[0].lower()) < 3 or levenshtein('amstrong'.lower(), row[0].lower()) < 5:
#             print ('\t' + row[0])
#         if 'Battelle'.lower() in row[0].lower():

        # if 'Leidos'.lower() in row[0].lower():
        #     print ('\t' + row[0])
