# Author tbejos

def sum():
    last = 1
    cur = 2
    sum = 2 2 
    while cur < 4000000:
            temp = cur
            cur += last
            last = temp
            if cur % 2 == 0:
                    sum += cur
    print(sum)
sum()
