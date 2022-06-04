# -- # -- # -- # -- # -- # -- | - | Longest Collatz sequence | - | -- # -- # -- # -- # -- # -- # 
                                           Problem 14  


The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.


# -- # -- # -- # -- # -- # -- | - |  MY ANSWER | - | # -- # -- # -- # -- # -- #

I wrote my answer for the set of numbers up to the entered x number, not the set of numbers below one million.


a=int(input()) 
chain_number=[]
for i in range(1,a):
    count=0
    while i>1:
            if i%2==0:
                i=i//2
                count=count+1

            else:
                i%2==1
                i=i*3+1
                count=count+1
    chain_number.append(count)
print(max(chain_number))
b= chain_number.index(max(chain_number))
print(b)