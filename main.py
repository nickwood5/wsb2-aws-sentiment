import threading, os
from apply_models import calculate_sentiment

class thread(threading.Thread):
   def __init__(self, index, file_name):
      threading.Thread.__init__(self)
      self.index = index
      self.file_name = file_name
   def run(self):
      print("{}: Running thread for {}".format(self.index, self.file_name))
      calculate_sentiment(self.index, self.file_name)



# Create new threads



tweet_plks = [f for f in os.listdir("input") if f.endswith("--tweets.plk")]
print("The files are {}".format(tweet_plks))

threads = []

for i, p in enumerate(tweet_plks):
   new_thread = thread(i, p)
   threads.append(new_thread)
   print("Applying models to {}".format(p))

for t in threads:
   t.start()


