from tqdm import tqdm
import time
for i in tqdm(range(50)):
    print(f"{i}/50")
    time.sleep(0.1)
    