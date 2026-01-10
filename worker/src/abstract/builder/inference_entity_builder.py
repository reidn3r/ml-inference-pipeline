from src.database.models.inference_entity import InferenceEntity

class InferenceEntityBuilder:
  def __init__(self):
    self.model_id = None
    self.input_id = None
    self.request_id = None
    self.prediction_content = None
    self.prediction_score = None
    self.inference_time_ms = None

  @staticmethod
  def create():
    return InferenceEntityBuilder()
  
  def withModelId(self, model_id):
    self.model_id = model_id
    return self

  def withInputId(self, input_id):
    self.input_id = input_id
    return self

  def withRequestId(self, request_id):
    self.request_id = request_id
    return self

  def withPredictionContent(self, prediction_content):
    self.prediction_content = prediction_content
    return self

  def withPredictionScore(self, prediction_score):
    self.prediction_score = prediction_score
    return self

  def withInferenceTimeMs(self, inference_time_ms):
    self.inference_time_ms = inference_time_ms
    return self

   
  def build(self):
    return InferenceEntity(
      model_id=self.model_id,
      input_id=self.input_id,
      request_id=self.request_id,
      prediction_content=self.prediction_content,
      prediction_score=self.prediction_score,
      inference_time_ms=self.inference_time_ms,
    )
  
  def __repr__(self):
    return (
        f"InferenceEntity("
        f"id={self.id}, "
        f"model_id={self.model_id}, "
        f"input_id={self.input_id}, "
        f"request_id='{self.request_id}', "
        f"prediction_content='{self.prediction_content}', "
        f"prediction_score={self.prediction_score}, "
        f"inference_time_ms={self.inference_time_ms}"
        f")"
    )

