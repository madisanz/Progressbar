# Progress Bar
from tqdm.auto import tqdm 

for i in tqdm(range(100001)):
    print(" ", end='\r')