import json
import numpy as np
import matplotlib.pyplot as plt
from watson_developer_cloud import ToneAnalyzerV3

emotions = []
bad_mood = True

def checkMood(tweets):
    """
    This funciton compares a users more recent posts to their older posts
    to estimate what kind of mood they are in. If they are in a bad mood it
    will return True
    """
    for tweet in tweets:
        analyzer(tweet)        
    return bad_mood


emotions = []     

tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    iam_apikey='key',
    url='https://gateway-wdc.watsonplatform.net/tone-analyzer/api'
)



def analyzer(tweet):
    """
    This function analyzes the mood of a tweet and returns an array of 5 different tones that
    the tweet can contain
    """

    emotion = [0.0, 0.0, 0.0, 0.0, 0.0]

    text = tweet

    tone_analysis = tone_analyzer.tone(
        {'text': text},
        'application/json'
    ).get_result()
    items = tone_analysis['document_tone']['tones']
    for item in items:
        
        if(item['tone_name'] == "Anger"):
            emotion[0] = item['score'] * (-1)
        if(item['tone_name'] == "Fear"):
            emotion[1] = item['score'] * (-1)
        if(item['tone_name'] == "Sadness"):
            emotion[2] = item['score'] * (-1)
        if(item['tone_name'] == "Confidence"):
            emotion[3] = item['score']
        if(item['tone_name'] == "Joy"):
            emotion[4] = item['score']

        # bad  = True if i >= 10 else False
        # bad_mood = bad

    emotions.append(emotion)


print(emotions)


def graph(tweets):
    """
    This function graphs the tone of the tweets after their mood has been found
    """
    anger = list(row[0] for row in emotions)
    fear = list(row[1] for row in emotions)
    sadness = list(row[2] for row in emotions)
    confident = list(row[3] for row in emotions)
    joy = list(row[4] for row in emotions)

    names = ['threshold', 'anger', 'fear', 'sadness', 'confidence', 'joy']

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

    #Create Graph
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
    plt.savefig('output.png')

#testing
# analyzer("I am scared of ghost")
# analyzer("I love here")
# graph()
# print(emotions)

# print(json.dumps(tone_analysis, indent=2))
