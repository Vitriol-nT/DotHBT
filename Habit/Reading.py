from Encoding_hbt import decode_custom

file1 = "habit.hbt"
OnceUsed1 = False

def read(file):
    with open(file, "rb") as f:
        BareByte = f.readline()
        Processed = decode_custom(BareByte)
        itprd = Processed.split('\n')
        print(itprd)
    return itprd