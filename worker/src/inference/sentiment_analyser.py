from transformers import pipeline
from config.logger import logger

class SentimentAnalyser:
  def __init__(self):      
    self.name = "nlptown/bert-base-multilingual-uncased-sentiment"
    
    self.model = pipeline(
      "sentiment-analysis",
      model=self.name,
    )
  
  def run(self, text: str):
    try:
      result = self.model(text[:512])[0]  
      label, score = result['label'], result['score']

      logger.info(f"Inferece Label: {label}",);
      logger.info(f"Inferece Score: {score}",);
      return label, score
    
    except Exception as e:
      logger.error(f'Error: {e}')
