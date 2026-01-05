from transformers import pipeline

class SentimentAnalyser:
  def __init__(self):      
    self.model = pipeline(
      "sentiment-analysis",
      model="nlptown/bert-base-multilingual-uncased-sentiment",
    )

    self.name = "nlptown/bert-base-multilingual-uncased-sentiment"
  
  def run(self, text: str):
    try:
      result = self.model(text[:512])[0]  
      label, score = result['label'], result['score']

      print("[MODEL]: Label:", label, flush=True);
      print("[MODEL]: Score:", score, flush=True);
      return label, score
    
    except Exception as e:
      print(e)
