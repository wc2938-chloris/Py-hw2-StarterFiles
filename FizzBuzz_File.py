import numpy as np

def FizzBuzz(start, finish):
    v = []
    for i in np.arange (start, finish + 1):
        if i % 15 == 0:
            v.append('fizzbuzz')
        elif i % 3 == 0:
            v.append('fizz')
        elif i % 5 == 0:
            v.append('buzz')
        else:
            v.append(int(i))

    return(v)

print(FizzBuzz(40, 45))
