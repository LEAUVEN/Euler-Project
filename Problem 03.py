# -- # -- # -- # -- # -- # -- | - | Largest prime factor | - | -- # -- # -- # -- # -- # -- # 

Task:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

# -- # -- # -- # -- # -- # -- | - |  MY ANSWER | - | # -- # -- # -- # -- # -- #

m=2
sayi=600851475143
while m**2<sayi:
    while sayi%m==0:
        sayi=sayi/m
    m=m+1
print(int(sayi))

Output>>>6857