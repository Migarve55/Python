
def is_prime(x):
    if x <= 1:
        return False
    for n in range(1,x+1):
        if x % n == 0 and n != 1 and x != n: 
            return False
            break
    else:
        return True

while True:
    inputString = input("Número: ") 
    if is_prime(int(inputString)):
        print("Es primo")
    else:
        print("No es primo")
