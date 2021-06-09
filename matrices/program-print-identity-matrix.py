# Program for Identity Matrix https://www.geeksforgeeks.org/program-print-identity-matrix/

def Identity(size):
    for row in range(0, size):
        for col in range(0, size):
 
            # Here end is used to stay in same line
            if (row == col):
                print("1 ", end=" ")
            else:
                print("0 ", end=" ")
        print()


Identity(10)