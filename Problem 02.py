# -- # -- # -- # -- # -- # -- | - | Even Fibonacci numbers | - | -- # -- # -- # -- # -- # -- # 

Task:

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# -- # -- # -- # -- # -- # -- | - |  MY ANSWER | - | # -- # -- # -- # -- # -- #

fibonacciSeries = [0,1]
toplam=[]
if 4000000>2:
    for i in range(2, 4000000):
        nextElement = fibonacciSeries[i-1] + fibonacciSeries[i-2]
        fibonacciSeries.append(nextElement)
        if nextElement>4000000: break    
for i in fibonacciSeries:
    if i%2==0:
        toplam.append(i)
sum(toplam)

OUTPUT>>>> 4613732