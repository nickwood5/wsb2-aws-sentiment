import os
from multiprocessing import Process
from apply_models import calculate_sentiment

# Create new threads
if __name__ == '__main__':
   tweet_plks = [f for f in os.listdir("input") if f.endswith("--tweets.plk")]
   print("The files are {}".format(tweet_plks))

   threads = []

   for i, p in enumerate(tweet_plks):
      Process(target=calculate_sentiment, args=[i, p]).start()
      print("Applying models to {}".format(p))


