import random
import time

n=1000000
l=[random.uniform(0.,1.) for _ in range(n)]
print(l)

start_time = time.time()
maximum = l[0]
for element in l:
    if element > maximum:
        maximum = element

end_time = time.time()

print(f"il massimo è {maximum}")
print(f"tempo esecuzione: {end_time-start_time}")