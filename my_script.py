from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

def scoresForString(sentence):
  scores = analyser.polarity_scores(sentence)
  return "{:-<60} {}".format(sentence, str(scores))

  
print(scoresForString("I like cats, they're the best."))