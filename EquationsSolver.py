
def get_eq(raw_eq):
    result = raw_eq
    return result

def get_vals(eq):
    vals = []
    for i in range(len(eq)):
        if eq[i] == '-' or eq[i] == '+':
            eq[i] = ' '
    for spt in eq.split():
        vals.append(spt)
    return vals

def solve(matrix):
    solves = []
    detM = 1
    for s in matrix:
        pass
    return solves

def print_solves(sol):
    for n in range(len(sol)):
        print("Val %i: %s" % (n + 1,sol[n]))

loop = True
equations = []
matrix = []

while loop:
    print("Enter all your equations, enter '!' when done")
    inp = ''
    
    while inp != '!':
        inp = input("Enter the next equation: ")
        if inp != '!':
            equations.append(get_eq(inp))

    print("Procesing...")
    for eq in equations:
        matrix.append(get_vals(eq))

    print_solves(solve(matrix))
    equations = []
    matrix = []
    


    
