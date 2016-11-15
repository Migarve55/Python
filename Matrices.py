
M1 = [[1,-3,0],[4,-2,6],[7,1,-4]]
M2 = [[0,5,2],[1,0,4],[0,2,2]]
M3 = [[0,5,2],[1,0,4],[0,2]] #Esta matriz no es valida aposta
M4 = [[3,2,2],[1,-2,4],[2,3,-2]]

#Crear matrizes

def printMatrix(m):
    for row in m:
        print(' '.join(str(row)))

def newMatrix(i,j): #Rectangulares
    new = []
    new_row = []
    for a in range(i):
        for b in range(j):
            new_row.append(0)
        new.append(new_row)
        new_row = []
    return new

def newSquareMatrix(o): #Cuadradas
    new = []
    new_row = []
    for a in range(o):
        for b in range(o):
            new_row.append(0)
        new.append(new_row)
        new_row = []
    return new

def newIdentMatrix(o): #Identidad
    new = []
    new_row = []
    for i in range(o):
        for e in range(o):
            if i == e:
                new_row.append(1)
            else:
                new_row.append(0)
        new.append(new_row)
        new_row = []
    return new

def newTMatrix(o, t): #Triangular superior o inferiror 
    new = newSquareMatrix(o)
    for i in range(o):
            for n in range(i,o):
                if t == 's':
                    new[i][n] = 1
                elif t == 'i':
                    new[n][i] = 1
    return new

# Cualidades de matrizes

def isMatrix(m):
    row_num = len(m[0])
    for n in m:
        if len(n) != row_num:
            return False
    return True

def matrixSize(m):
    if not isMatrix(m):
        return 'e'
    return len(m), len(m[0]) #Row_Number, Col_Number

def det(m):
    d = 0
    if not (isMatrix(m) and len(m) == len(m[0])):
        return 'e'
    return d

def matrixRange(m):
    Range = 0
    if not isMatrix(m):
        return 'e'
    if len(m) > len(m[0]):
        maxRange = len(m[0])
    else:
        maxRange = len(m)

    for checkRange in range(maxRange):
        for i in range(len(m)):
            for j in range(len(m[0])):
                if checkRange == 0:
                    if m[i][j] != 0:
                        Range = 1
                        break
                    else:
                        pass
    return Range

# Transformaciones de matrices

def trans(m):
    if not isMatrix(m):
        return 'e'
    new = newMatrix(len(m),len(m[0]))
    for i in range(len(m)):
        for j in range(len(m[0])):
            new[i][j] = m[j][i]
    return new   

def adj(m,x,y):
    if not isMatrix(m):
        return 'e'
    new = []
    new_row = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if not (i == x or j == y):
                new_row.append(m[i][j])
        new.append(new_row)
        new_row = []
    return det(new)

def adjMatrix(m):
    if not isMatrix(m):
        return 'e'
    new = []
    new_row = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            new_row.append(((-1)^(i + j)) * adj(m,i,j))
        new.append(new_row)
        new_row = []
    return new

# Operaciones entre matrizes
 
def addMatrix(m1,m2):
    result_row = []
    result_m = []
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            result_row.append(m1[i][j] + m2[i][j]);
        result_m.append(result_row)
        result_row = []
    return result_m

def multiplyByNumber(num, m):
    result_row = []
    result_m = []
    for n in m:
        for c in n:
            print(c)
            result_row.append(int(c * num))
        result_m.append(result_row)
        result_row = []      
    return result_m

def multiplyMatrix(m1,m2):
    result_row = []
    result_m = []
    c = 0
    if not (isMatrix(m1) and isMatrix(m2)):
        return "Error one of the matrix given is not a matrix"
    elif len(m1[0]) != len(m2):
        return 'Error matrix given are not operable with each other'
    for i in range(len(m1)): #Por cada fila de la primera
        for j in range(len(m2[0])): #Por cada columna de la segunda
            for k in range(len(m1)):
                c += m1[i][k] * m2[k][j]
            result_row.append(c)
            c = 0
        result_m.append(result_row)
        result_row = []
    return result_m

def inv(m):
    if not isMatrix(m):
        return 'e'
    return multiplyByNumber(1 / det(m), trans(adjMatrix(m)))

#print(matrixSize(M4))
#printMatrix(multiplyMatrix(M4,newIdentMatrix(3)))
#printMatrix(multiplyByNumber(6, M4))
#print(isMatrix(M3))
#printMatrix(newTMatrix(4,'s'))
#printMatrix(newTMatrix(5,'i'))
#printMatrix(trans(M1))

print("Done")


