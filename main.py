dial = 50


number = 70
counter = 0

dial = (dial - number) % 100
if dial -  number < 0:
    counter += 1

dial = (dial + number) % 100
if dial + number > 100:
    counter +=1


print(dial)
print(counter)
