import codecs,sys

blockSize = 1048576
with codecs.open(sys.argv[1],"r",encoding="mbcs") as sourceFile:
    with codecs.open(sys.argv[1]+".utf8.json","w",encoding="UTF-8") as targetFile:
        while True:
            contents = sourceFile.read(blockSize)
            if not contents:
                break
            targetFile.write(contents)