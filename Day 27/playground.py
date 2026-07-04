def add(*numbers):
    sum = 0
    for n  in numbers:
        sum += n
    return sum
print(add(1,2,3,4,5))