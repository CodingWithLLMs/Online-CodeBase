def isPowerOfThree(n):
    if n<1:
        return False
    while n%3==0:
        n//=3
    return n==1