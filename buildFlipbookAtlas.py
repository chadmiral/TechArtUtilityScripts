import sys, os
from PIL import Image

inputDir = sys.argv[1]
outputFile = sys.argv[2]

outDim =  [ int(sys.argv[3]), int(sys.argv[4]) ]
outCount = [ int(sys.argv[5]), int(sys.argv[6]) ]

print("Input directory: " + inputDir)
print("Output file: " + outputFile)

outImg = Image.new('RGBA', (outDim[0], outDim[1]))

i = 0
j = 0
for subdir, dirs, files in os.walk(inputDir):
    for file in files:
        filepath = subdir + os.sep + file
        print ("loading " + filepath)
        img = Image.open(filepath)

        newSize = (int(outDim[0] / outCount[0]), int(outDim[1] / outCount[1]))
        img = img.resize(newSize)

        outImg.paste(img, (i * newSize[0], j * newSize[0]))

        #worst way to do this, but IDGAF
        i = i + 1
        if(i >= outCount[0]):
            i = 0
            j = j+1


outImg.save(outputFile)