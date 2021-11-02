# Alice-Bob

## Alice and Bob prime number communication game; python script
```
$ python alice+bob.py
hello BoB

prime number p = 53
prime number q = 37
N = 1961

I have a number c where gcd(c,1872)=1 , c = ?  y/n
> n
c =  5
d =  749

I have Alice Public Key ?  y/n
> n
Alice Public Key b =  526

.
.
.
connection established
message recieved a =  134
```
## LargePrimeNumbers_runtime.ipynb
The larger the prime number, the more complicated and impossible the problem becomes.

for 4 digits it would take ~ 200849654 centuries

## QTeleportation.ipynb (Quantum solution)
Alice wants to transfers an unknown quantum state $\\Psi$ 
* Alice and Bob use a third party : Telamon
   * TELAMON : send an entangled qubit pair

   * ALICE : using one entangled pair of qubits shared by TELAMON, she sends the results to BOB over a classical communication channel.

   * BOB : prefoms some operation based on the classical information sent by ALICE
