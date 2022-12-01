import glob

dir = input("Directory:")
sch = input("Search keyword:")

if not (dir.endswith("/")):
    dir+="/"

fls = glob.glob(dir+"*")
cantread = []
foundat = []

for fname in fls:
    try:
        f = open(fname, "r")
        lines = f.readlines()
        for l in lines:
            if sch in l:
                loc = fname + ":\t" + str(lines.index(l)+1)
                foundat.append(loc)
    except:
        cantread.append(fname)

if len(foundat) == 0:
    print("Not found")
else:
    print("Found at:")
    for l in foundat:
        print("\t",l)

if len(cantread) != 0:
    print("Can't read file(s):")
    for f in cantread:
        print("\t",f)

