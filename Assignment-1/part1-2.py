# This function returns whether or not the first
# string is a permutation of the second string. 
def isStringPermutation(s1: str, s2: str) -> bool:
    for char in s1:
        if char not in s2:
            return False
    
    return True

def pairsThatEqualSum(inputArray: list, targetSum: int) -> list:
    ret_pairs = []

    for i in range(len(inputArray)):
        for j in range(i+1, len(inputArray)):
            if inputArray[i] + inputArray[j] == targetSum:
                ret_pairs.append((inputArray[i], inputArray[j]))
    
    return ret_pairs

print(pairsThatEqualSum([1, 2, 3, 4, 5], 1))