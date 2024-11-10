def writeNumbersOfFibonacci(n):
    result = ""
    a=0
    b=1
    counter=2
    result += "{0}. item= {1}\n".format(counter-1,a)
    result += "{0}. item= {1}\n".format(counter,b)

    for i in range(3,n+1):
        c=a+b
        counter+=1
        result += "{0}. item= {1}\n".format(counter,c)
        a=b
        b=c
    return result

n = int(input("Enter a number: "))
n=int(n)

donut=writeNumbersOfFibonacci(n)
print(donut)