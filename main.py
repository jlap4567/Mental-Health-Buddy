import helper

textFile = open('testData.txt', 'r')
for line in textFile:
    helper.analyzer(line)
textFile.close()

helper.graph()