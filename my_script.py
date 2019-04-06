from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

def scoresForString(sentence):
  scores = analyser.polarity_scores(sentence)
  return "{:-<60} {}".format(sentence, str(scores))

  
print(scoresForString("those people don't understand me, it makes me feel like something is wrong with me"))
print(scoresForString("I really like Elaina, she's amazing!"))