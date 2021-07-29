## ==========================
## ===> HELPER FUNCTIONS <===
## ==========================
## ---> GLOBAL VARIABLES <---
FOLDERNAME = "arrayandstrings/"

## ---> readfile <---
## INPUT:
##  filename (str): Name of file to load (do NOT include ".txt")
##  varSize (bool): If 'False' just returns a list, if 'True' then
##                  the data will be a matrix, first line indicates
##                  number of rows, with that many rows following
##                  which belong to the matrix. See
##                  "testRotateMatrix.txt" for an example.
## OUTPUT:
##  data (list):    Either a normal list or a list of matrices
##                  depending on varSize.
## COMMENTS: standard function for reading in data from the test files.
def readfile(filename, varSize):
    data = []
    with open(FOLDERNAME + filename + ".txt", 'r') as f:
        if varSize:
            line = f.readline()
            while line:
                line = line.strip()
                nRow = int(line)
                matrix = []
                for iRow in range(nRow):
                    row = f.readline()
                    row = row.strip()
                    matrix.append(row.split())
                data.append(matrix)
                line = f.readline()
        else:
            for line in f:
                line = line.rstrip()
                data.append(line)
    return data

## ---> printmatrix <---
## INPUT:
##  matrix: a mxn matrix
## OUPUT:
##  (void)
## COMMENT: prints the matrix in a nice grid pattern
## TEST:
##  printmatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
def printmatrix(matrix):
    for row in matrix:
        for entry in row:
            print(str(entry) + '\t', end="")
        print("\n")
    return

## ---> booltostr <---
## COMMENT: Takes the boolean value 'b' and turns it
##          into the string "true" or "false".
def booltostr(b):
    if b:
        return "true"
    else:
        return "false"
