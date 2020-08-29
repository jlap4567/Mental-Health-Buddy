import helper

textFile = open('./assets/testData.txt', 'r')
for line in textFile:
    helper.analyzer(line)
textFile.close()

helper.graph()