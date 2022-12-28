import pandas as pd, os
from vader_sentiment import sentiment
from emotions import get_emotion
from time import time


file_name = "2020-08-21 00_00_00_2020-08-31 00_00_00--tweets.plk"

def calculate_sentiment(file_name):
    loop_range = 100
    average = 0

    start_time = time()
    input_file = "input/" + file_name

    data = pd.read_pickle(input_file)

    all_compounds = []
    all_overall_sentiments = []
    all_emotions = []

    loop = 0

    loop_start = time()

    for i, c in enumerate(data["content"]):
        compound, overall_sentiment = sentiment(c)
        #print("{} of {}, compound = {}".format(i+1, len(data), compound))

        all_compounds.append(compound)
        all_overall_sentiments.append(overall_sentiment)

        emotion = get_emotion(c)
        all_emotions.append(emotion)

        loop += 1

        if loop >= loop_range:
            loop_end = time()

            elapsed_time = loop_end - loop_start

            average = elapsed_time / loop_range
            remaining = len(data) - (i + 1)
            estimated_time = remaining * average
            
            print("{} of {}, est. time remaining: {}s".format(i+1, len(data), round(estimated_time, 0)))
            loop = 0
            

            loop_start = loop_end

    data["sentiment_score"] = all_compounds
    data["sentiment_label"] = all_overall_sentiments
    data["emotion_label"] = all_emotions

    output_file = "output/SENTIMENTS_" + file_name

    data.to_pickle(output_file, compression='infer', protocol=5, storage_options=None)

    print(data)
    end_time = time()

    print(start_time)
    print(end_time)


tweet_plks = [f for f in os.listdir("input") if f.endswith("--tweets.plk")]
for p in tweet_plks:
    calculate_sentiment(p)

