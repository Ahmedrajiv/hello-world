for i in [1,2,3,4,5]:
    print (i)
for i in range (10):
    print(i)
for i in range (5,11):
    print (i)
for i in range (1,20,2):
    print(i)

#printing even no.s using while loop!!!
i=0
while (i<=10):
    print (i)
    i=i+2

#Continue Statement
a=[1,2,3,4,5,6,7,8,9]
for i in a:
    if (i%2==0):
        print (i,"even")
        continue
    else:
        print (i,"odd")


#break statement
a=[1,2,3,4,5,6,7,8,9]
for i in a:
    if (i%2==0):
        print (i,"even")
        break
    else:
        print (i,"odd")



