import json
import numpy as np
import matplotlib.pyplot as plt
from watson_developer_cloud import ToneAnalyzerV3

emotions = []
def checkMood(tweets):
    """
    This funciton compares a users more recent posts to their older posts
    to estimate what kind of mood they are in. If they are in a bad mood it
    will return True
    """
    return True

emotions = []     

tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    iam_apikey='UIgXJXk48P1YLymIbkEN1it5pMac0XVnLMh6Bv-PGEsr',
    url='https://gateway-wdc.watsonplatform.net/tone-analyzer/api'
)



def analyzer(tweet):

    emotion = [0.0, 0.0, 0.0, 0.0, 0.0]

    text = tweet

    tone_analysis = tone_analyzer.tone(
        {'text': text},
        'application/json'
    ).get_result()
    items = tone_analysis['document_tone']['tones']
    for item in items:
        if(item['tone_name'] == "Anger"):
            emotion[0] = item['score']*(-1)
        if(item['tone_name'] == "Fear"):
            emotion[1] = item['score']*(-1)
        if(item['tone_name'] == "Sadness"):
            emotion[2] = item['score']*(-1)
        if(item['tone_name'] == "Confident"):
            emotion[3] = item['score']
        if(item['tone_name'] == "Joy"):
            emotion[4] = item['score']

    emotions.append(emotion)


print(emotions)


def graph():
    anger = list(row[0] for row in emotions)
    fear = list(row[1] for row in emotions)
    sadness = list(row[2] for row in emotions)
    confident = list(row[3] for row in emotions)
    joy = list(row[4] for row in emotions)

    names = ['threshold', 'anger', 'fear', 'sadness', 'confident', 'joy']

    print(anger)
    print(fear)
    print(sadness)
    print(confident)
    print(joy)

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
    D = np.array(confident)
    E = np.array(joy)

    plt.axhline(y=0, linestyle='--', color='black')

    plt.bar(X, A, color='red', align='center')
    plt.bar(X, B, color='purple', bottom=A, align='center')
    plt.bar(X, C, color='blue', bottom=A + B, align='center')
    plt.bar(X, D, color='green', align='center')
    plt.bar(X, E, color='yellow', bottom=D, align='center')

    

    plt.legend(names, loc=2, fancybox=True, framealpha=0.5)
    plt.ylim([-3, 2])
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

#testing
# analyzer("I am scared of ghost")
# analyzer("I love here")
# graph()
# print(emotions)

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
