from math import fabs

def reverseArray(value):
    return value[::-1]

def mulPoly(s1, s2):
    res = [0]*(len(s1)+len(s2)-1)
    
    for o1,i1 in enumerate(s1):
        for o2,i2 in enumerate(s2):
            res[o1+o2] += i1*i2

    for o1, i1 in enumerate(res):
        if(i1 % 2 == 0):
            res[o1] = 0
        else:
            res[o1] = 1
    
    return res

def addPoly(s1, s2):
    if len(s1) > len(s2):
        res = [0]*len(s1)
        remaining = len(s1)-len(s2)
        for x in range(remaining):
            s2.append(0)
        for o1 in range(len(s1)):
            if((s1[o1] + s2[o1]) % 2 == 0):
                res[o1] = 0
            else:
                res[o1] = 1
        
    else:
        res = [0]*len(s2)
        remaining = len(s2)-len(s1)
        for x in range(remaining):
            s1.append(0)
        for o1 in range(len(s2)):
            if((s1[o1] + s2[o1]) % 2 == 0):
                res[o1] = 0
            else:
                res[o1] = 1

    return res

def check(remainder):
    if(len(remainder) == 1 and remainder[0] == 1):
        return False
    else:
        return True

def findInverse(value):
    GF = [1, 1, 0, 1, 1, 0, 0, 0, 1] #in reverse order to calculate for polynomial values
    t0 = [0]
    t1 = [1]
    t2 = [0]
    quotient, remainder = poly_div(GF, value)
    while check(remainder):
        GF, value = value, remainder
        t2 = addPoly(t0, mulPoly(t1, quotient))
        t1, t0 = t2, t1
        quotient, remainder = poly_div(GF, value)
        
    GF = value
    remainder = 0
    print(GF, value)
    t2 = addPoly(t0, mulPoly(t1, quotient))
    counter = 0
    binValue = ''
    while(counter < 8):
        binValue += str(t2[counter])
        counter += 1
    
    binValue = binValue[::-1]
    print(binValue)
    return hex(int(binValue, 2))

def degree(poly):
    while poly and poly[-1] == 0:
        poly.pop()   # normalize
    return len(poly)-1

def poly_div(N, D):
    dD = degree(D)
    dN = degree(N)
    if dD < 0: raise ZeroDivisionError
    if dN >= dD:
        q = [0] * dN
        while dN >= dD:
            d = [0]*(dN - dD) + D
            mult = q[dN - dD] = N[-1] / float(d[-1])
            d = [coeff*mult for coeff in d]
            N = [fabs ( coeffN - coeffd ) for coeffN, coeffd in zip(N, d)]
            dN = degree(N)
        r = N
    else:
        q = [0]
        r = N
    return q, r

def hextobin(hexval):

    thelen = len(hexval)*4
    binval = bin(int(hexval, 16))[2:]
    while ((len(binval)) < thelen):
        binval = '0' + binval

    binArray = list(binval[::-1])
    desired_array = [int(numeric_string) for numeric_string in binArray]
    return desired_array
    
    

value = input("Enter a hex value: ")
inverse = findInverse(hextobin(value))
print('The inverse is: ', inverse[2::].upper())


