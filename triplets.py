import math

def formula(a,b,c):
    formula22 = a-b*math.sqrt(c)

    if formula22 > 0:
        (1. / 3.0)
        form22calc = math.pow(formula22, float(1)/3)    
    else:
        form22calc = -math.pow(abs(formula22), float(1)/3)

    calc = math.pow(a+b*math.sqrt(c), float(1)/3.0) + form22calc
    return calc
    
count = 0

for a in range(1,998):
    for b in range(1,998):
        for c in range (1,998):
            if a+b+c <= 110000000:
                calc = formula(a,b,c)
                if str(calc)== "1.0":
                    print str(calc)
                    print "("+str(a)+","+str(b)+","+str(c)+") = "+str(calc)
                    count+=1
                    print count
