import random
import defs

# initialization array
array = []
for i in range(10):
    array.append(random.randint(1, 50))
    print(array[i])

# finding minimum number
print('Minimum element:', defs.find_minimum(array))

# finding average number
print('Average number: ', defs.find_avg(array))



