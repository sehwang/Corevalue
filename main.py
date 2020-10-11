

def make_db():

    source = []
    f = open("Coval.txt", 'r')
    lines = f.readlines()
    for line in lines:
        words = line.split(", ")
        source.append(words)
    f.close()

    DB = []
    for k in source:
        #print(k)
        #print(k[2])
        i = 0
        while i <= int(k[2]):
            i += 1



make_db()


print("\ndone")
