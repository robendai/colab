import time
from random import randint

start_time = time.time()
for i in range(0,99999):
    print(i)

print("--- %s seconds ---" % (time.time() - start_time))
