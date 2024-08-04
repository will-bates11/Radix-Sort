items = [4, 1, 5, 3, 2]
    
sortItems = radix_sort(items)
# sortItems is [1, 2, 3, 4, 5]
    
print(items)
print(sortItems)
    
# *** simplified speed test ***
items = list(range(1, 200))
items[5], items[6] = items[6], items[5]
count = 1000
start = datetime.now()
    
for n in range(1, count):
    radix_sort(items)
    
delta = datetime.now() - start
totalMicroseconds = delta.seconds * 1000000 + delta.microseconds

print(totalMicroseconds)
# about 281_498 microseconds

