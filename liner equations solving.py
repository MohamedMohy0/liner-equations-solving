from calendar import c
import numpy as np
k="yes"
while k=="yes":
    try:
        a=[[],[]]  #you can add more empty lists it debends on how many equations
        b=[]
        for i in range(0,2):#change the range debends on how many equations
            for u in range(0,2):#change the range debends on how many equations
                z=eval(input("enter the cof:"))
                a[i].append(z)
            c=eval(input("enter the answar:"))
            b.append(c)
        A = np.array(a)
        B = np.array(b)
        x = np.linalg.solve(A, B)
        print(x)
    except NameError:
        print("please input only a numper")
    except :
        print("there is infinty solution or no solution")
    k=input("are you want to try agian?:")
    if k=="yes":
        print("lets try another time")
    elif k=="no":
        print("program finihed")
    else:
        print("invaild input")