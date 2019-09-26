import os

names = []
fts = 0
bb = 0
def printPyNames(dpath, KeyWord):
    global names
    global fts
    global bb
    if os.path.isfile(dpath) and KeyWord not in dpath:
        print("你他妈的别乱逼逼~~")
        bb += 1
    elif os.path.isfile(dpath) and KeyWord in dpath:
        fts += 1
        # names.append(dpath)
        names.append(dpath.strip().split('\\').pop())
    elif os.path.isdir(dpath):
        for ds in os.listdir(dpath):
            newdir = os.path.join(dpath, ds)
            printPyNames(newdir, KeyWord)

if __name__ == '__main__':
    dpath = "G:\\黄大宝python\\2018"
    KeyWord = "PyTrade_fbap"
    printPyNames(dpath, KeyWord)
    print("--------------------------------------------->>[%d]" %len(names))
    print(names)
    print("--------------------------------------------->>[%d]" % len(set(names)))
    
    print(bb)