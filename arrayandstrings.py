import helperfunction as h

## ===========================================
## ===> INTERVIEW QUESTION IMPLEMENTATION <===
## ===========================================
def isunique(string):
    strSorted   = sorted(string)
    nStr        = len(strSorted)
    for i in range(nStr-1):
        if strSorted[i] == strSorted[i+1]:
            return False
    return True

def checkpermutation(str1, str2):
    nStr = len(str1)
    if nStr != len(str2):
        return False
    str1Sorted = sorted(str1)
    str2Sorted = sorted(str2)
    for i in range(nStr):
        if str1Sorted[i] != str2Sorted[i]:
            return False
    return True

def urlify(string, nStr):
    string  = string[0:nStr]
    urlSep  = "%20"
    return string.replace(" ", "%20")

def palindromePerm(string):
    string  = string.lower()
    charArr  = sorted(string)
    while len(charArr) and charArr[0] == ' ':
        del charArr[0:1]
    foundMid  = False
    while len(charArr) > 1:
        if charArr[0] == charArr[1]:
            del charArr[0:2]
        elif not foundMid:
            foundMid = True
            del charArr[0:1]
        else:
            return False
    return (len(charArr) == 0) or not foundMid

def oneaway(str1, str2):
    if len(str1) > len(str2):
        str1, str2 = str2, str1
    nStr1 = len(str1)
    nStr2 = len(str2)
    if (nStr1+1) == nStr2:
        foundDel = False
        for i in range(nStr1):
            if not foundDel:
                if str1[i] != str2[i]:
                    foundDel = True
            else:
                if str1[i] != str2[i+1]:
                    return False
        return True
    elif nStr1 == nStr2:
        foundRep = False
        for i in range(nStr1):
            if str1[i] != str2[i]:
                if not foundRep:
                    foundRep = True
                else:
                    return False
        return True
    return False

def strcompress(string):
    nStr = len(string)
    compressedStr = ""
    currentChar = string[0]
    count = 0
    for c in string:
        if c == currentChar:
            count += 1
        else:
            compressedStr += currentChar + str(count)
            count = 1
            currentChar = c
    compressedStr += currentChar + str(count)
    if len(compressedStr) < nStr:
        return compressedStr
    return string

def rotatematrix(matrix):
    n = len(matrix)
    nHalf = (n+1)//2
    newMatrix = [[0] * n for i in range(n)]
    for i in range(nHalf):
        for j in range(nHalf):
            newMatrix[i][j]         = matrix[n-j-1][i]
            newMatrix[j][n-i-1]     = matrix[i][j]
            newMatrix[n-i-1][n-j-1] = matrix[j][n-i-1]
            newMatrix[n-j-1][i]     = matrix[n-i-1][n-j-1]
    return newMatrix

def zeromatrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    newMatrix = [[0] * n for i in range(m)]

    isZeroRow = [False] * m
    isZeroCol = [False] * n
    for row in range(m):
        for col in range(n):
            if int(matrix[row][col]) == 0:
                isZeroRow[row] = True
                isZeroCol[col] = True
    for row in range(m):
        for col in range(n):
            if not isZeroRow[row] and not isZeroCol[col]:
                newMatrix[row][col] = matrix[row][col]
    return newMatrix

def strrotation(str1, str2):
    return str1 in (str2 + str2)

## ==============
## ===> MAIN <===
## ==============
def main():
    folderName = "arrayandstrings/"
    h.FOLDERNAME = folderName

    print("[TEST] 1.1 Is Unique")
    dataIsUnique = h.readfile("testIsUnique", 0)
    for data in dataIsUnique:
        isUnique = isunique(data)
        isUnique = h.booltostr(isUnique)
        print("\'" + data + "\' is unique?\t " + isUnique)

    print("\n[TEST] 1.2 Check Permutation")
    dataCheckPermutation = h.readfile("testCheckPermutation", 0)
    for s in dataCheckPermutation:
        s1, s2 = s.split()
        isPerm = checkpermutation(s1,s2)
        isPerm = h.booltostr(isPerm)
        print("\'" + s1 + "\' is permutation of \'" + s2 + "\'?\t " + isPerm)

    print("\n[TEST] 1.3 URLify")
    dataUrlify = h.readfile("testUrlify", 0)
    for s in dataUrlify:
        string, nStr = s.split(", ")
        nStr = int(nStr)
        sUrlified = urlify(string, nStr)
        print("\'" + string + "\' becomes:" + sUrlified)

    print("\n[TEST] 1.4 Palindrome Permutation")
    dataPalPerm = h.readfile("testPalPerm", 0)
    for s in dataPalPerm:
        isPalPerm = palindromePerm(s)
        isPalPerm = h.booltostr(isPalPerm)
        print("\'" + s + "\' is permutation of a palindrome? " + isPalPerm)

    print("\n[TEST] 1.5 One Away")
    dataOneAway = h.readfile("testOneAway", 0)
    for strPair in dataOneAway:
        s1, s2 = strPair.split()
        isOneAway = oneaway(s1, s2)
        isOneAway = h.booltostr(isOneAway)
        print("Are \'" + s1 + "\' and  \'" + s2 + "\' one away?\t " + isOneAway)

    print("\n[TEST] 1.6 String Compression")
    dataStrCompress = h.readfile("testStrCompress", 0)
    for s in dataStrCompress:
        compressed = strcompress(s)
        print("\'" + s + "\' compresses to:" + compressed)

    print("\n[TEST] 1.7 Rotate Matrix")
    dataRotateMatrix = h.readfile("testRotateMatrix", 1)
    for matrix in dataRotateMatrix:
        matrixRotated = rotatematrix(matrix)
        print("Original Matrix:")
        h.printmatrix(matrix)
        print("Matrix Rotated CW 90 Degrees:")
        h.printmatrix(matrixRotated)

    print("\n[TEST] 1.8 Zero Matrix")
    dataZeroMatrix = h.readfile("testZeroMatrix", 1)
    for matrix in dataZeroMatrix:
        matrixZeroed = zeromatrix(matrix)
        print("Original Matrix:")
        h.printmatrix(matrix)
        print("Matrix w/ Zero-ed Rows and Columns:")
        h.printmatrix(matrixZeroed)

    print("\n[TEST] 1.9 String Rotation")
    dataStrRotation = h.readfile("testStrRotation", 0)
    for sPair in dataStrRotation:
        s1, s2 = sPair.split()
        isRotation = strrotation(s1, s2)
        isRotation = h.booltostr(isRotation)
        print("\'" + s2 + "\' is a rotation of  \'" + s2 + "\'?\t " + isRotation)

    return

if __name__ == "__main__":
    main()
