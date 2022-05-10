'''variables is like storage containers of values'''
'''variables are reusable in python '''

a=5
print(a)
a=6
print(a)
print(a);print(a)  #every print statement new value 6                                                    6
print(a,a)  #6 6
'''1st way of assigning values to variables'''

p=1
q=2
r=3
s=4
print(p)   #1 2 3 4 in vartical
print(q)
print(r)
print(s)
''' ; is called terminator which means totally ending of the line'''
''' , is a used for seperation which takes sigle/one space'''
print(p);print(q);print(r);print(s) #1 2 3 4 in vartical
print(p),print(q),print(r),print(s) #1 2 3 4 in vartical
print(p,q,r,s)  # in horizontal direction 1 2 3 4 

'''2nd way of assigning values to variables'''
p=1;q=2;r=3;s=4
print(p,q,r,s)#1 2 3 4

'''3rd way of assigning values to variables'''
p=q=5;r=6;s=4
print(p,q,r,s)#5 5 6 4

'''4th way of assigning values to variables'''
p,q,r,s=1,2,3,4
print(p,q,r,s)#1 2 3 4

'''ERRORS OCCURED WHILE ASSIGNING VARIABLES AND VALUES'''
'''VALUE ERROR'''
p,q,r,s=1,2,3
print(p,q,r,s)   #ValueError: not enough values to unpack (expected 4, got 3) 
#not enough values are given to the variables

p,q,r,s=1,2,3,4,5
print(p,q,r,s) #too many values to unpack (expected 4)
#more no of values are there compare to variables

'''NAME ERROR'''
a=6
b=5
c=a+b
print(d)#NameError: name 'd' is not defined
#variable d is not defined
