Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for i in range(9,0,-1): 
    for j in range(i,0,-1): 
        print(i,"*",j,"=",i*j," ",'\t',end='') 
    print(end='\n') 
