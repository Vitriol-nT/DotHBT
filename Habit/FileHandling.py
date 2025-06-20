import os
from Encoding_hbt import encode_custom

file1 = "habit.hbt"
OnceUsed1 = False

def save(habit):
    global OnceUsed1
    size = os.path.getsize(file1)
    with open(file1, mode='ab') as f:
        if OnceUsed1 == False:
            f.write(encode_custom(f"{habit}\n"))
            OnceUsed1 = True
        elif OnceUsed1 == True:
            f.write(encode_custom(f"{habit}\n"))
        elif size > 10:
            OnceUsed1 = True