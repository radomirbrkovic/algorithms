# Jacobsthal and Jacobsthal-Lucas numbers https://www.geeksforgeeks.org/jacobsthal-and-jacobsthal-lucas-numbers/

def Jacobsthal(n):
    # base case
    if (n == 0):
        return 0
 
    # base case
    if (n == 1):
        return 1
 
    # recursive step.
    return Jacobsthal(n - 1) + 2 * Jacobsthal(n - 2)
 
# Return nth Jacobsthal-Lucas number.
def Jacobsthal_Lucas(n):
    # base case
    if (n == 0):
        return 2
         
    # base case
    if (n == 1):
        return 1
 
    # recursive step.
    return Jacobsthal_Lucas(n - 1) + 2 * Jacobsthal_Lucas(n - 2)
 
# Driven Program
n = 5
print("Jacobsthal number:", Jacobsthal(n))
print("Jacobsthal-Lucas number:", Jacobsthal_Lucas(n))