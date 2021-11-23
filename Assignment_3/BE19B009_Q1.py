def delta(a, b):
    """
    Return the cost value according to the substitution
    Purines by Purines ==> 1
    Pyrimidines by Pyrimidines ==> 1
    Purines by Pyrimidines ==> 3
    Purines by Pyrimidines ==> 3
    """

    pur = ["A", "G"]
    pyr = ["T", "C"]

    if (a == b):
        return 0

    if (a in pur and b in pur or a in pyr and b in pyr):
        return 1

    if (a in pur and b in pyr or a in pyr and b in pur):
        return 3

def min_mutation(s, t):

    INS = 2             # insertion cost = 2
    DEL = 2             # deletion cost = 2

    edTab = [[0 for i in range(len(s) + 1)] for j in range(len(t) + 1)]

    for i in range(1, len(s) + 1):
        edTab[0][i] = i*INS         # first row can only be inserted

    for j in range(1, len(t) + 1):
        edTab[j][0] = j*DEL         # first column can only be deleted

    for i in range(1, len(t) + 1):
        for j in range(1, len(s) + 1):
            DELTA = delta(s[j-1], t[i-1])       # calculate the substitution cost

            # Finding the minimum of the insertion, deletion, substitution
            edTab[i][j] = min(edTab[i][j-1] + INS, edTab[i-1][j] + DEL, edTab[i-1][j-1] + DELTA)

    print(edTab[-1][-1])                        # print edit distance
    

min_mutation("ATGC", "ATGGG")
min_mutation("TAGTA", "TGGTA")



