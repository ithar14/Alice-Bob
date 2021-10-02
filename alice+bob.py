import math
import random

#-----------BOB----------
print("hello BoB \n")
p = int(input("prime number p = "))
q = int(input("prime number q = "))

N = p*q
print("N =",N)

x = (p-1)*(q-1)

#////find c//////
answer1 = input("\nI have a number c where gcd(c,{})=1 , c = ?  y/n \n".format(x))
if answer1 == "y" :
    # input c
    c = int(input("c = "))
else :
    for i in range (2,N): 
        if math.gcd(i,x)==1:
            c = i
            break
    print("c = ",c)

#////find d//////
for i in range(1,N):
    f = (1+x*i)/c
    if f % int(f)==0:
        d=int(f)
        break
print("d = ",d)

#-----------ALICE----------
answer2 = input("\nI have Alice Public Key ?  y/n \n")
if answer2 == "y":
    # input b
    b = int(input("\nAlice Public Key b = "))
else :
    # find a 
    a_alice = random.randint(1, N-1)
    #print("a_alice =",a_a)

    # find b
    b = (a_alice**c) % N
    print("Alice Public Key b = ",b)


#-----------BOB----------
#////find a//////
a_bob = (b**d)%N


if answer2 == "y" : 
    print("\n.\n.\n.\nAlice sent = ",a_bob)
else :
    # check connection
    if a_alice ==a_bob :
        print("\n.\n.\n.")
        print("connection established")
        print("message recieved a = ",a_bob)
    else :
        print("connection Timed out \n could not connect")
