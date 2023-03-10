import pandas as pd, os, sys
from vader_sentiment import sentiment
from emotions import get_emotion
from time import time


file_name = "2020-08-21 00_00_00_2020-08-31 00_00_00--tweets.plk"

def calculate_sentiment(index, file_name):
    loop_range = 100
    average = 0

    start_time = time()
    input_file = "input/" + file_name

    data = pd.read_pickle(input_file)

    all_compounds = []
    all_overall_sentiments = []
    all_happy = []
    all_angry = []
    all_sad = []
    all_fear = []
    all_surprise = []

    loop = 0

    loop_start = time()

    for i, c in enumerate(data["content"]):
        compound, overall_sentiment = sentiment(c)

        all_compounds.append(compound)
        all_overall_sentiments.append(overall_sentiment)

        emotions = get_emotion(c)
        happy = emotions["Happy"]
        angry = emotions["Angry"]
        sad = emotions["Sad"]
        fear = emotions["Fear"]
        surprise = emotions["Surprise"]

        all_happy.append(happy)
        all_angry.append(angry)
        all_sad.append(sad)
        all_fear.append(fear)
        all_surprise.append(surprise)

        loop += 1

        if loop >= loop_range:
            loop_end = time()

            elapsed_time = loop_end - loop_start

            average = elapsed_time / loop_range
            remaining = len(data) - (i + 1)
            estimated_time = remaining * average
            
            print("{}: {} of {}, est. time remaining: {}s".format(index, i+1, len(data), round(estimated_time, 0)), flush=True)
            loop = 0
            

            loop_start = loop_end
        sys.stdout.flush()

    data["sentiment_score"] = all_compounds
    data["sentiment_label"] = all_overall_sentiments
    data["happy"] = all_happy
    data["fear"] = all_fear
    data["angry"] = all_angry
    data["sad"] = all_sad
    data["surprise"] = all_surprise


    output_file = "output/SENTIMENTS_" + file_name

    data.to_pickle(output_file, compression='infer', protocol=5, storage_options=None)

    print("{}: {}".format(index, data), flush=True)
    end_time = time()

    print("{}: started at {}".format(index, start_time), flush=True)
    print("{}: ended at {}".format(index, end_time), flush=True)

    sys.stdout.flush()


#tweet_plks = [f for f in os.listdir("input") if f.endswith("--tweets.plk")]
#print("The files are {}".format(tweet_plks))
#for p in tweet_plks:
#    print("Applying models to {}".format(p))
#    calculate_sentiment(p)

