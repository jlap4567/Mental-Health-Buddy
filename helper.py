import json
import numpy as np
import matplotlib.pyplot as plt
from watson_developer_cloud import ToneAnalyzerV3

emotions = []     

tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    iam_apikey='UIgXJXk48P1YLymIbkEN1it5pMac0XVnLMh6Bv-PGEsr',
    url='https://gateway-wdc.watsonplatform.net/tone-analyzer/api'
)

emotion = [0.0,0.0,0.0]

text = 'Team, I know that times are tough! Product '\
    'sales have been stupidly disappointing for the past three '\
    'quarters. We have a competitive product, but we '\
    'need to do a better job of selling it!'

tone_analysis = tone_analyzer.tone(
    {'text': text},
    'application/json'
).get_result()
items = tone_analysis['document_tone']['tones']
for item in items:
    if(item['tone_name']=="Anger"):
        emotion[0] = item['score']
    if(item['tone_name']=="Fear"):
        emotion[1] = item['score']
    if(item['tone_name']=="Sadness"):
        emotion[2] = item['score']

emotions.append(emotion)
emotions.append([0.5, 0.3, 0.7])
emotions.append([0.1,0.2,0.3])

print(emotions)

anger = list(row[0] for row in emotions)
fear =  list(row[1] for row in emotions)
sadness = list(row[2] for row in emotions)

names = ['anger', 'fear', 'sadness']

print(anger)
print(fear)
print(sadness)

plt.figure()

# xanger= list(range(0,len(anger)))
# xsad= list(range(0,len(sadness)))
# xfear = list(range(0,len(fear)))
# plt.bar(xanger,anger,color="red",align = "center")
# plt.bar(xsad,sadness,color="blue",bottom = anger, align = "center")
# plt.bar(xfear,fear,color="green",bottom = anger+sadness, align = "center")

X = np.arange(len(emotions))

A = np.array(anger)
B = np.array(fear)
C = np.array(sadness)

plt.bar(X, A, color = 'red', align='center')
plt.bar(X, B, color = 'green', bottom = A, align='center')
plt.bar(X, C, color = 'blue', bottom = A + B, align='center')

plt.legend(names, loc=2)
plt.tick_params(
    axis='x',         
    which='both',      
    bottom=False,      
    top=False,         
    labelbottom=False)
plt.xlabel('tweets')
plt.ylabel('mood')
plt.title('Mood rating over time')
# plt.show()
plt.savefig('foo.png')

# print(json.dumps(tone_analysis, indent=2))



# # evenly sampled time at 200ms intervals
# t = np.arange(0., 5., 0.2)

# # red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# 

# Import the libraries
# import matplotlib.pyplot as plt
# import seaborn as sns

# # matplotlib histogram
# plt.hist(flights['arr_delay'], color = 'blue', edgecolor = 'black',
#          bins = int(180/5))

# # seaborn histogram
# sns.distplot(flights['arr_delay'], hist=True, kde=False, 
#              bins=int(180/5), color = 'blue',
#              hist_kws={'edgecolor':'black'})
# # Add labels
# plt.title('Histogram of Arrival Delays')
# plt.xlabel('Delay (min)')
# plt.ylabel('Flights')
# plt.show()