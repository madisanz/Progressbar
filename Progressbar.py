
# Progress Bar

from tqdm.auto import tqdm 

for i in tqdm(range(100001)):
    print(" ", end='\r')
  

# With tqdm (conda install tqdm or pip install tqdm) 
# I can add a progress meter to my loops in a second:

from time import sleep
from tqdm import tqdm
for i in tqdm(range(10)):
    sleep(3)
