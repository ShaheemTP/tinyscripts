from os import listdir, getcwd
from os.path import isfile, join

onlyfiles = []
onlydirs = []
cantread = []
foundat = []
comms = []

dir = input("Directory:")
if dir.startswith("~"):
    dir = getcwd() + dir[1:]
"""if not (dir.endswith("/")):
       dir+="/"   """

try:
    allfiles = listdir(dir)
except:
    print("Can't read the directory: \""+dir+"\"\nAre you sure it exists?")
    exit()

sch = input("Search keyword:")
comm = input("Comments start with:")

for f in allfiles:
    fname = join(dir, f)
    if isfile(fname):
        onlyfiles.append(fname)
    else:
        onlydirs.append(fname)

def searchin(f, comm):
    lines = f.readlines()
    for l in lines:
        if sch in l:
            loc = fname + ":\t" + str(lines.index(l)+1)
            if(comm != "NA" and l.startswith(comm)):
                comms.append(loc)
            else:
                foundat.append(loc)

for fname in onlyfiles:
    try:
        f = open(fname, "r")
        searchin(f, comm)
    except:
        cantread.append(fname)

if (len(foundat) == 0) and (len(comms) == 0):
    print("Not found",end="")
else:
    if len(foundat) != 0:
        print("Found at:")
        for i in range(1, len(foundat)+1):
            print("\t",foundat[i-1],end="")
            if (i%2) == 0:
                print("\n",end="")            
    if len(comms) != 0:
        print("\nIn comments:")
        for i in range(1, len(comms)+1):
            print("\t",comms[i-1],end="")
            if (i%2) == 0:
                print("\n",end="")

if len(cantread) != 0:
    print("\nCan't read file(s):")
    for i in range(1, len(cantread)+1):
        print("\t",cantread[i-1],end="")
        if (i%3) == 0:
            print("\n",end="")

if len(onlydirs) != 0:
    print("\nThese are directories, not regural files:")
    for i in range(1, len(onlydirs)+1):
        print("\t",onlydirs[i-1],end="")
        if (i%3) == 0:
            print("\n",end="")

print("\nExited")
